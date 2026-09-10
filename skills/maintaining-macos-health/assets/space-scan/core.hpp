#pragma once
#include <algorithm>
#include <cstdint>
#include <cstring>
#include <limits>
#include <queue>
#include <stdexcept>
#include <string>
#include <string_view>
#include <utility>
#include <vector>

namespace fastscan {
// Darwin attribute wire identifiers; the macOS translation unit static_asserts
// these against the installed SDK. No native structs are cast onto wire data.
namespace wire {
constexpr uint32_t name=0x00000001, type=0x00000008, flags=0x00040000;
constexpr uint32_t fileid=0x02000000, error=0x20000000, returned=0x80000000;
constexpr uint32_t mount=0x00000004, links=0x00000001, total=0x00000002, alloc=0x00000004;
constexpr uint32_t common=name|type|flags|fileid|error|returned;
constexpr uint32_t file=links|total|alloc;
}
inline uint64_t add(uint64_t a, uint64_t b) {
    if (b > std::numeric_limits<uint64_t>::max()-a)
        throw std::overflow_error("byte/count total exceeds uint64_t");
    return a+b;
}
class Cursor {
    const unsigned char* data_; size_t size_, pos_=0;
public:
    Cursor(const void* data,size_t size):data_(static_cast<const unsigned char*>(data)),size_(size){}
    size_t position() const { return pos_; }
    template<class T> T read() {
        if(pos_>size_ || sizeof(T)>size_-pos_) throw std::runtime_error("truncated attribute record");
        T result{}; std::memcpy(&result,data_+pos_,sizeof result); pos_+=sizeof result; return result;
    }
};
struct Entry {
    uint32_t length=0, common=0, directory=0, file=0, error=0;
    uint32_t type=0, flags=0, mount=0, links=0;
    uint64_t inode=0;
    int64_t logical=-1, allocated=-1;
    std::string_view name;
};
// Parses options=0 records: only attributes marked returned occupy space.
// ATTR_CMN_ERROR is the special field immediately after RETURNED_ATTRS.
inline Entry decode(const void* buffer,size_t available) {
    Cursor prefix(buffer,available); Entry e; e.length=prefix.read<uint32_t>();
    if(e.length<24 || e.length>available) throw std::runtime_error("invalid attribute record length");
    Cursor c(buffer,e.length); (void)c.read<uint32_t>();
    e.common=c.read<uint32_t>(); const auto vol=c.read<uint32_t>();
    e.directory=c.read<uint32_t>(); e.file=c.read<uint32_t>(); const auto fork=c.read<uint32_t>();
    if((e.common&~wire::common) || vol || (e.directory&~wire::mount) || (e.file&~wire::file) || fork)
        throw std::runtime_error("unexpected returned attribute mask");
    if(!(e.common&wire::returned)) throw std::runtime_error("missing RETURNED_ATTRS");
    if(e.common&wire::error) e.error=c.read<uint32_t>();
    size_t ref=0; int32_t offset=0; uint32_t length=0;
    if(e.common&wire::name) { ref=c.position(); offset=c.read<int32_t>(); length=c.read<uint32_t>(); }
    if(e.common&wire::type) e.type=c.read<uint32_t>();
    if(e.common&wire::flags) e.flags=c.read<uint32_t>();
    if(e.common&wire::fileid) e.inode=c.read<uint64_t>();
    if(e.directory&wire::mount) e.mount=c.read<uint32_t>();
    if(e.file&wire::links) e.links=c.read<uint32_t>();
    if(e.file&wire::total) e.logical=c.read<int64_t>();
    if(e.file&wire::alloc) e.allocated=c.read<int64_t>();
    if(e.common&wire::name) {
        const int64_t start=static_cast<int64_t>(ref)+offset;
        if(start<static_cast<int64_t>(c.position()) || !length ||
           start>e.length || length>e.length-static_cast<size_t>(start))
            throw std::runtime_error("invalid name reference");
        const char* p=static_cast<const char*>(buffer)+start;
        if(p[length-1]!='\0' || std::memchr(p,'\0',length-1)) throw std::runtime_error("invalid name terminator");
        e.name=std::string_view(p,length-1);
        if(e.name.find('/')!=std::string_view::npos) throw std::runtime_error("slash in entry name");
    }
    return e;
}
struct Row {
    uint64_t logical=0, allocated=0, inode=0; uint32_t links=1; std::string path;
};
class TopK {
    struct Better {
        bool allocated=true;
        bool operator()(const Row& a,const Row& b) const {
            auto x=allocated?a.allocated:a.logical, y=allocated?b.allocated:b.logical;
            return x!=y?x>y:a.path<b.path; // priority_queue top is the worst retained row.
        }
    };
    size_t limit_; Better better_; std::priority_queue<Row,std::vector<Row>,Better> heap_;
public:
    TopK(size_t limit,bool allocated):limit_(limit),better_{allocated},heap_(better_){}
    bool may_enter(uint64_t logical,uint64_t allocated) const {
        if(!limit_) return false;
        if(heap_.size()<limit_) return true;
        return (better_.allocated?allocated:logical)>=(better_.allocated?heap_.top().allocated:heap_.top().logical);
    }
    void offer(Row row) {
        if(!limit_) return;
        if(heap_.size()<limit_) heap_.push(std::move(row));
        else if(better_(row,heap_.top())) { heap_.pop(); heap_.push(std::move(row)); }
    }
    std::vector<Row> sorted() const {
        auto copy=heap_; std::vector<Row> rows; rows.reserve(copy.size());
        while(!copy.empty()) { rows.push_back(copy.top()); copy.pop(); }
        std::sort(rows.begin(),rows.end(),better_); return rows;
    }
};
struct Totals { uint64_t logical=0,allocated=0,files=0,errors=0,excluded=0; };
inline void merge(Totals& a,const Totals& b) {
    a.logical=add(a.logical,b.logical); a.allocated=add(a.allocated,b.allocated);
    a.files=add(a.files,b.files); a.errors=add(a.errors,b.errors); a.excluded=add(a.excluded,b.excluded);
}
// Parent must precede child, as ensured by the scanner's discovery order.
inline void aggregate(std::vector<Totals>& totals,const std::vector<size_t>& parents) {
    if(totals.size()!=parents.size()) throw std::invalid_argument("tree arrays differ in length");
    for(size_t i=totals.size();i>1;) { --i; if(parents[i]>=i) throw std::invalid_argument("invalid parent order"); merge(totals[parents[i]],totals[i]); }
}
inline std::string json_string(std::string_view s) {
    static constexpr char hex[]="0123456789abcdef";
    std::string out="\"";
    for(unsigned char ch:s) {
        if(ch=='"' || ch=='\\') { out+='\\'; out+=static_cast<char>(ch); }
        else if(ch<0x20 || ch==0x7f) { out+="\\u00"; out+=hex[ch>>4]; out+=hex[ch&15]; }
        else out+=static_cast<char>(ch);
    }
    return out+'"';
}
} // namespace fastscan

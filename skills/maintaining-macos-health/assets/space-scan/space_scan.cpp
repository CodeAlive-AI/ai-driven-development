// Read-only macOS metadata scanner. Not an APFS raw-device reader.
#ifndef __APPLE__
#error "space_scan requires macOS; core_tests.cpp can run on other platforms."
#endif
#include "core.hpp"
#include <sys/attr.h>
#include <sys/mount.h>
#include <sys/stat.h>
#include <sys/vnode.h>
#include <unistd.h>
#include <fcntl.h>
#include <dirent.h>
#include <cerrno>
#include <chrono>
#include <condition_variable>
#include <cstdlib>
#include <deque>
#include <filesystem>
#include <exception>
#include <iomanip>
#include <iostream>
#include <memory>
#include <mutex>
#include <thread>
#include <unordered_map>
#include <unordered_set>

using namespace fastscan;
static_assert(ATTR_CMN_NAME==wire::name && ATTR_CMN_OBJTYPE==wire::type && ATTR_CMN_FLAGS==wire::flags);
static_assert(ATTR_CMN_FILEID==wire::fileid && ATTR_CMN_ERROR==wire::error && ATTR_CMN_RETURNED_ATTRS==wire::returned);
static_assert(ATTR_FILE_LINKCOUNT==wire::links && ATTR_FILE_TOTALSIZE==wire::total && ATTR_FILE_ALLOCSIZE==wire::alloc);
static_assert(ATTR_DIR_MOUNTSTATUS==wire::mount && sizeof(off_t)==8 && sizeof(fsobj_type_t)==4);
struct FD {
    int value=-1;
    explicit FD(int fd=-1):value(fd){}
    ~FD(){if(value>=0) close(value);}
    FD(const FD&)=delete; FD& operator=(const FD&)=delete;
};
struct Options {
    unsigned workers=4; size_t top=50,buffer=256*1024;
    bool allocated=true,once=true,json=false,stat_backend=false,tree=false; std::string root;
    std::vector<std::string> exclusions;
};
struct Directory {
    Directory* parent=nullptr; size_t index=0; uint64_t inode=0;
    std::string name; Totals direct;
};
struct Hardlink { Row row; Directory* parent=nullptr; };
struct Local {
    TopK top; uint64_t entries=0,bulk_calls=0,fallback_stats=0,skipped_nonregular=0;
    Local(const Options& o):top(o.top,o.allocated){}
};
class Scanner {
    Options options_; std::string root_; FD rootfd_; fsid_t fsid_{};
    std::mutex mutex_,hard_mutex_; std::condition_variable ready_;
    std::deque<Directory*> queue_; std::vector<std::unique_ptr<Directory>> dirs_;
    std::unordered_set<uint64_t> seen_dirs_;
    std::unordered_map<uint64_t,Hardlink> hardlinks_;
    std::vector<std::string> warning_samples_; uint64_t hardlink_paths_=0;
    size_t pending_=0; std::exception_ptr failure_;
    std::vector<std::unique_ptr<Local>> locals_;
    static bool samefs(const fsid_t& a,const fsid_t& b) { return a.val[0]==b.val[0] && a.val[1]==b.val[1]; }
    std::string relative(const Directory* d) const {
        std::vector<std::string_view> parts;
        while(d->parent) { parts.emplace_back(d->name); d=d->parent; }
        std::string out;
        for(auto i=parts.rbegin();i!=parts.rend();++i) { if(!out.empty())out+='/'; out.append(i->data(),i->size()); }
        return out.empty()?".":out;
    }
    std::string full(const Directory* d) const {
        auto rel=relative(d); return rel=="."?root_:(root_=="/"?root_+rel:root_+"/"+rel);
    }
    static std::string childpath(const std::string& base,std::string_view name) {
        return base+(base=="/"?"":"/")+std::string(name);
    }
    bool excluded(const std::string& path) const {
        for(const auto& prefix:options_.exclusions)
            if(path==prefix || (path.size()>prefix.size() && path.compare(0,prefix.size(),prefix)==0 && path[prefix.size()]=='/')) return true;
        return false;
    }
    void warning(Directory* d,const std::string& path,const std::string& message) {
        d->direct.errors=add(d->direct.errors,1);
        std::lock_guard<std::mutex> lock(mutex_);
        if(warning_samples_.size()<20) warning_samples_.push_back(path+": "+message);
    }
    void enqueue(Directory* parent,std::string_view name,uint64_t inode) {
        std::lock_guard<std::mutex> lock(mutex_);
        if(!seen_dirs_.insert(inode).second) { parent->direct.excluded=add(parent->direct.excluded,1); return; }
        auto d=std::make_unique<Directory>(); d->parent=parent; d->index=dirs_.size(); d->inode=inode; d->name=name;
        auto* ptr=d.get(); dirs_.push_back(std::move(d)); queue_.push_back(ptr); ++pending_; ready_.notify_one();
    }
    bool restat(int fd,std::string_view name,Entry& e,Local& local) {
        ++local.fallback_stats; struct stat st{}; std::string n(name);
        if(fstatat(fd,n.c_str(),&st,AT_SYMLINK_NOFOLLOW)!=0) return false;
        e.type=S_ISDIR(st.st_mode)?VDIR:S_ISREG(st.st_mode)?VREG:S_ISLNK(st.st_mode)?VLNK:VNON;
        e.inode=st.st_ino; e.flags=st.st_flags; e.links=st.st_nlink;
        e.logical=st.st_size;
        e.allocated=(st.st_blocks<0 || static_cast<uint64_t>(st.st_blocks)>static_cast<uint64_t>(INT64_MAX)/512)
                    ?-1:static_cast<int64_t>(st.st_blocks)*512;
        // stat fallback measures stat's size/block accounting, not necessarily all forks.
        e.common|=wire::type|wire::fileid|wire::flags; e.file|=wire::file;
        return true;
    }
    void consume(Directory* parent,int fd,const std::string& base,Entry e,Local& local) {
        if(e.name.empty()) {
            warning(parent,base,e.error?"entry error: "+std::string(strerror(e.error)):"entry has no usable name");
            return;
        }
        if(e.name=="." || e.name=="..") return;
        ++local.entries;
        const auto required=wire::type|wire::fileid|wire::flags;
        bool missing=(e.common&required)!=required || !e.inode;
        if(e.type==VREG && ((e.file&wire::file)!=wire::file || e.logical<0 || e.allocated<0 || !e.links)) missing=true;
        if(e.error || missing) {
            if(!restat(fd,e.name,e,local)) { warning(parent,childpath(base,e.name),strerror(errno)); return; }
        }
        if(e.type==VDIR) {
            if(!options_.exclusions.empty() && excluded(childpath(base,e.name))) { ++parent->direct.excluded; return; }
            if((e.directory&wire::mount) && (e.mount&(DIR_MNTSTATUS_MNTPOINT|DIR_MNTSTATUS_TRIGGER))) {
                ++parent->direct.excluded; return;
            }
#ifdef SF_FIRMLINK
            if(e.flags&SF_FIRMLINK) { ++parent->direct.excluded; return; }
#endif
#ifdef SF_DATALESS
            if(e.flags&SF_DATALESS) { warning(parent,childpath(base,e.name),"dataless directory skipped (local-only policy)"); return; }
#endif
            enqueue(parent,e.name,e.inode); return;
        }
        if(e.type!=VREG) { ++local.skipped_nonregular; return; }
        if(e.logical<0 || e.allocated<0 || !e.links) { warning(parent,childpath(base,e.name),"invalid file metadata"); return; }
        const auto logical=static_cast<uint64_t>(e.logical), allocated=static_cast<uint64_t>(e.allocated);
        if(options_.once && e.links>1) {
            Row row{logical,allocated,e.inode,e.links,childpath(base,e.name)};
            std::lock_guard<std::mutex> lock(hard_mutex_); ++hardlink_paths_;
            auto it=hardlinks_.find(e.inode);
            if(it==hardlinks_.end()) hardlinks_.emplace(e.inode,Hardlink{std::move(row),parent});
            else if(row.path<it->second.row.path) it->second=Hardlink{std::move(row),parent};
            return;
        }
        merge(parent->direct,Totals{logical,allocated,1,0,0});
        if(local.top.may_enter(logical,allocated)) local.top.offer(Row{logical,allocated,e.inode,e.links,childpath(base,e.name)});
    }
    void fallback_directory(Directory* d,int fd,const std::string& base,Local& local) {
        // A separately opened descriptor is required: never mix readdir and bulk
        // on the same open file description / offset.
        int copy=openat(fd,".",O_RDONLY|O_DIRECTORY|O_CLOEXEC);
        if(copy<0) { warning(d,base,strerror(errno)); return; }
        DIR* stream=fdopendir(copy);
        if(!stream) { int err=errno;close(copy);warning(d,base,strerror(err));return; }
        try {
            for(;;) {
                errno=0; dirent* de=readdir(stream);
                if(!de) { if(errno)warning(d,base,strerror(errno)); break; }
                Entry e; e.name=de->d_name; // consume uses fstatat only in this fallback.
                consume(d,dirfd(stream),base,e,local);
            }
        } catch(...) { closedir(stream); throw; }
        closedir(stream);
    }
    void scan_directory(Directory* d,Local& local,std::vector<unsigned char>& buffer) {
        auto rel=relative(d),base=full(d);
        int flags=O_RDONLY|O_DIRECTORY|O_CLOEXEC;
#ifdef O_NOFOLLOW_ANY
        // Darwin rejects combining O_NOFOLLOW_ANY and O_NOFOLLOW (EINVAL).
        flags|=O_NOFOLLOW_ANY;
#else
        flags|=O_NOFOLLOW;
#endif
        FD fd(openat(rootfd_.value,rel.c_str(),flags));
        if(fd.value<0) { warning(d,base,strerror(errno)); return; }
        struct stat st{}; struct statfs fs{};
        if(fstat(fd.value,&st)!=0 || fstatfs(fd.value,&fs)!=0) { warning(d,base,strerror(errno));return; }
        if(!samefs(fs.f_fsid,fsid_)) { ++d->direct.excluded;return; }
        if(st.st_ino!=d->inode) { warning(d,base,"directory changed identity during scan");return; }
#ifdef SF_DATALESS
        if(st.st_flags&SF_DATALESS) { warning(d,base,"dataless directory skipped before enumeration");return; }
#endif
        if(options_.stat_backend) { fallback_directory(d,fd.value,base,local);return; }
        attrlist attrs{};attrs.bitmapcount=ATTR_BIT_MAP_COUNT;
        attrs.commonattr=wire::common;attrs.dirattr=wire::mount;attrs.fileattr=wire::file;
        bool any=false;
        for(;;) {
            ++local.bulk_calls;
            int count=getattrlistbulk(fd.value,&attrs,buffer.data(),buffer.size(),0);
            if(count==0)break;
            if(count<0) {
                if(errno==EINTR)continue;
                if(!any && (errno==ENOTSUP || errno==EINVAL || errno==ENOSYS)) { fallback_directory(d,fd.value,base,local);return; }
                warning(d,base,strerror(errno)); return;
            }
            any=true;size_t offset=0;
            for(int i=0;i<count;++i) {
                Entry e=decode(buffer.data()+offset,buffer.size()-offset);
                offset+=e.length;consume(d,fd.value,base,e,local);
            }
        }
    }
    void worker(Local& local) {
        try {
            std::vector<unsigned char> buffer(options_.buffer);
            for(;;) {
                Directory* d;
                {
                    std::unique_lock<std::mutex> lock(mutex_);
                    ready_.wait(lock,[&]{return failure_ || !queue_.empty() || pending_==0;});
                    if(failure_ || pending_==0)return;
                    d=queue_.front();queue_.pop_front();
                }
                scan_directory(d,local,buffer);
                {std::lock_guard<std::mutex> lock(mutex_);--pending_;if(!pending_)ready_.notify_all();}
            }
        } catch(...) {
            std::lock_guard<std::mutex> lock(mutex_); if(!failure_)failure_=std::current_exception();ready_.notify_all();
        }
    }
    static void print_row_json(const Row& row) {
        std::cout<<"{\"logical_bytes\":"<<row.logical<<",\"allocated_bytes\":"<<row.allocated
                 <<",\"inode\":"<<row.inode<<",\"links\":"<<row.links<<",\"path\":"<<json_string(row.path)<<'}';
    }
public:
    explicit Scanner(Options options):options_(std::move(options)) {
        char* canonical=realpath(options_.root.c_str(),nullptr);
        if(!canonical)throw std::runtime_error("realpath: "+std::string(strerror(errno)));
        root_=canonical;free(canonical);
        for(auto& path:options_.exclusions) {
            std::filesystem::path candidate(path);
            if(!candidate.is_absolute())throw std::runtime_error("--exclude requires an absolute directory path");
            path=candidate.lexically_normal().string();
            while(path.size()>1 && path.back()=='/')path.pop_back();
            if(path=="/" || path==root_ || (root_.size()>path.size() && root_.compare(0,path.size(),path)==0 && root_[path.size()]=='/'))
                throw std::runtime_error("--exclude must not contain the scan root");
        }
        rootfd_.value=open(root_.c_str(),O_RDONLY|O_DIRECTORY|O_CLOEXEC|O_NOFOLLOW);
        if(rootfd_.value<0)throw std::runtime_error("open root: "+std::string(strerror(errno)));
        struct stat st{};struct statfs fs{};
        if(fstat(rootfd_.value,&st)!=0 || fstatfs(rootfd_.value,&fs)!=0)throw std::runtime_error(strerror(errno));
        if(!(fs.f_flags&MNT_LOCAL))throw std::runtime_error("this prototype only scans local mounted file systems");
        fsid_=fs.f_fsid;
        auto root=std::make_unique<Directory>();root->inode=st.st_ino;queue_.push_back(root.get());
        seen_dirs_.insert(st.st_ino);dirs_.push_back(std::move(root));pending_=1;
    }
    int run() {
        const auto start=std::chrono::steady_clock::now();std::vector<std::thread> threads;
        try {
            for(unsigned i=0;i<options_.workers;++i) {
                locals_.push_back(std::make_unique<Local>(options_));auto* local=locals_.back().get();
                threads.emplace_back([this,local]{worker(*local);});
            }
        } catch(...) {
            {std::lock_guard<std::mutex> lock(mutex_);failure_=std::current_exception();ready_.notify_all();}
        }
        for(auto& thread:threads)thread.join();if(failure_)std::rethrow_exception(failure_);
        TopK files(options_.top,options_.allocated),directories(options_.top,options_.allocated);
        uint64_t entries=0,calls=0,fallbacks=0,nonregular=0;
        for(auto& local:locals_) {
            entries+=local->entries;calls+=local->bulk_calls;fallbacks+=local->fallback_stats;nonregular+=local->skipped_nonregular;
            for(auto& row:local->top.sorted())files.offer(std::move(row));
        }
        for(auto& item:hardlinks_) {
            auto& h=item.second;merge(h.parent->direct,Totals{h.row.logical,h.row.allocated,1,0,0});files.offer(std::move(h.row));
        }
        std::vector<Totals> totals;std::vector<size_t> parents;totals.reserve(dirs_.size());parents.reserve(dirs_.size());
        for(auto& d:dirs_){totals.push_back(d->direct);parents.push_back(d->parent?d->parent->index:0);}
        aggregate(totals,parents);
        for(size_t i=1;i<dirs_.size();++i)if(directories.may_enter(totals[i].logical,totals[i].allocated))
            directories.offer(Row{totals[i].logical,totals[i].allocated,dirs_[i]->inode,1,full(dirs_[i].get())});
        const double seconds=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
        const auto& t=totals.front();auto frows=files.sorted(),drows=directories.sorted();
        if(options_.json) {
            std::cout<<"{\"root\":"<<json_string(root_)<<",\"engine\":"<<json_string(options_.stat_backend?"readdir-fstatat":"getattrlistbulk")<<",\"metric\":"<<json_string(options_.allocated?"allocated":"logical")
                     <<",\"hardlinks\":"<<json_string(options_.once?"once-canonical-path":"per-path")
                     <<",\"seconds\":"<<std::setprecision(8)<<seconds<<",\"entries\":"<<entries<<",\"directories\":"<<dirs_.size()
                     <<",\"counted_regular_files\":"<<t.files<<",\"logical_bytes\":"<<t.logical<<",\"allocated_bytes\":"<<t.allocated
                     <<",\"errors\":"<<t.errors<<",\"excluded_directories\":"<<t.excluded<<",\"skipped_nonregular\":"<<nonregular
                     <<",\"fallback_stat_calls\":"<<fallbacks<<",\"bulk_calls\":"<<calls
                     <<",\"hardlink_paths_seen\":"<<hardlink_paths_<<",\"hardlinked_inodes\":"<<hardlinks_.size()
                     <<",\"snapshot_consistent\":false,\"reclaimable_bytes\":null,\"files\":[";
            bool first=true;for(auto& row:frows){if(!first)std::cout<<',';first=false;print_row_json(row);}std::cout<<"],\"folders\":[";
            first=true;for(auto& row:drows){if(!first)std::cout<<',';first=false;print_row_json(row);}std::cout<<"],\"warning_samples\":[";
            first=true;for(auto& w:warning_samples_){if(!first)std::cout<<',';first=false;std::cout<<json_string(w);}std::cout<<"]";
            std::cout<<",\"exclusions\":[";
            first=true;for(const auto& path:options_.exclusions){if(!first)std::cout<<',';first=false;std::cout<<json_string(path);}std::cout<<']';
            if(options_.tree) {
                // Compact parent/name records: no repeated full paths, no file array.
                std::cout<<",\"folder_tree_version\":1,\"folder_tree\":[";
                for(size_t i=0;i<dirs_.size();++i) {
                    if(i)std::cout<<',';
                    const auto& row=totals[i];
                    std::cout<<'['<<parents[i]<<','<<json_string(i?dirs_[i]->name:root_)<<','<<row.logical<<','<<row.allocated<<','<<row.errors<<','<<row.excluded<<']';
                }
                std::cout<<']';
            }
            std::cout<<"}\n";
        } else {
            std::cout<<"Root: "<<json_string(root_)<<"\nRegular files counted: "<<t.files<<"; directories: "<<dirs_.size()
                     <<"; entries: "<<entries<<"\nLogical: "<<t.logical<<" bytes; allocated: "<<t.allocated<<" bytes\n"
                     <<"Elapsed: "<<std::fixed<<std::setprecision(3)<<seconds<<" s; bulk calls: "<<calls<<"; fallback stats: "<<fallbacks
                     <<"\nErrors: "<<t.errors<<"; excluded directories: "<<t.excluded<<"; skipped nonregular: "<<nonregular
                     <<"\nHardlinks: "<<(options_.once?"counted once, attributed to lexicographically first observed path":"counted for every path")
                     <<"\nAllocated bytes are NOT bytes that deletion is guaranteed to free. Live scan, not a snapshot.\n";
            for(const auto& group:{std::make_pair("FILES",&frows),std::make_pair("FOLDERS (excluding root)",&drows)}) {
                std::cout<<"\n"<<group.first<<"\n    allocated        logical  path\n";
                for(const auto& row:*group.second)std::cout<<std::setw(13)<<row.allocated<<' '<<std::setw(14)<<row.logical<<"  "<<json_string(row.path)<<'\n';
            }
            for(auto& w:warning_samples_)std::cerr<<"Warning: "<<json_string(w)<<'\n';
        }
        // Exit 2 means incomplete coverage; JSON/report is still usable.
        return t.errors?2:0;
    }
};
static unsigned long number(const char* text,unsigned long min,unsigned long max) {
    if(!text || *text=='-' || !*text)throw std::runtime_error("invalid numeric argument");
    char* end=nullptr;errno=0;auto n=strtoul(text,&end,10);
    if(errno || *end || n<min || n>max)throw std::runtime_error("numeric argument outside allowed range");return n;
}
int main(int argc,char** argv) {
    try {
        Options o;
        for(int i=1;i<argc;++i) {
            std::string a=argv[i];auto next=[&](){if(++i>=argc)throw std::runtime_error("missing value for "+a);return argv[i];};
            if(a=="--workers")o.workers=static_cast<unsigned>(number(next(),1,64));
            else if(a=="--backend") {std::string v=next();if(v!="bulk"&&v!="stat")throw std::runtime_error("backend must be bulk or stat");o.stat_backend=v=="stat";}
            else if(a=="--top")o.top=number(next(),1,1000000);
            else if(a=="--buffer-kib")o.buffer=number(next(),4,8192)*1024;
            else if(a=="--metric") {std::string v=next();if(v!="allocated"&&v!="logical")throw std::runtime_error("metric must be allocated or logical");o.allocated=v=="allocated";}
            else if(a=="--hardlinks") {std::string v=next();if(v!="once"&&v!="paths")throw std::runtime_error("hardlinks must be once or paths");o.once=v=="once";}
            else if(a=="--tree")o.tree=true;
            else if(a=="--exclude" || a=="-s")o.exclusions.emplace_back(next());
            else if(a=="--json")o.json=true;
            else if(a=="--help") {std::cout<<"space_scan [--backend bulk|stat] [--workers 1..64] [--top N] [--metric allocated|logical] [--hardlinks once|paths] [--buffer-kib 4..8192] [--json] [--tree] [--exclude ABSOLUTE_DIRECTORY] ROOT\n";return 0;}
            else if(!a.empty()&&a[0]=='-')throw std::runtime_error("unknown option: "+a);
            else if(!o.root.empty())throw std::runtime_error("specify exactly one root directory");else o.root=a;
        }
        if(o.root.empty())throw std::runtime_error("specify ROOT, e.g. \"$HOME\" or /System/Volumes/Data; see --help");
        if(o.tree&&!o.json)throw std::runtime_error("--tree requires --json");
        Scanner scanner(std::move(o));return scanner.run();
    } catch(const std::exception& e) {std::cerr<<"space_scan: "<<e.what()<<'\n';return 1;}
}

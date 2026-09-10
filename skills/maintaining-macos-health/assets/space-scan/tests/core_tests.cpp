#include "../core.hpp"
#include <cassert>
#include <iostream>
#include <random>
using namespace fastscan;
template<class T>void append(std::vector<unsigned char>& out,T v){size_t p=out.size();out.resize(p+sizeof v);std::memcpy(out.data()+p,&v,sizeof v);}
template<class T>void put(std::vector<unsigned char>& out,size_t p,T v){std::memcpy(out.data()+p,&v,sizeof v);}
std::vector<unsigned char> record(bool directory,bool error_only=false) {
    std::vector<unsigned char> b;append(b,uint32_t(0));
    auto common=error_only?(wire::returned|wire::error):wire::common;
    append(b,common);append(b,uint32_t(0));append(b,directory&&!error_only?wire::mount:uint32_t(0));
    append(b,!directory&&!error_only?wire::file:uint32_t(0));append(b,uint32_t(0));
    append(b,uint32_t(error_only?13:0));
    if(!error_only){
        const size_t ref=b.size();append(b,int32_t(0));append(b,uint32_t(6));
        append(b,uint32_t(directory?2:1));append(b,uint32_t(0));append(b,uint64_t(1234));
        if(directory)append(b,uint32_t(0));
        else {append(b,uint32_t(2));append(b,int64_t(10000));append(b,int64_t(4096));}
        put(b,ref,static_cast<int32_t>(b.size()-ref));
        for(char ch:std::string("a.txt"))b.push_back(static_cast<unsigned char>(ch));b.push_back(0);
    }
    while(b.size()%8)b.push_back(0);put(b,0,static_cast<uint32_t>(b.size()));return b;
}
template<class F>void must_throw(F f){bool thrown=false;try{f();}catch(const std::exception&){thrown=true;}assert(thrown);}
int main(){
    auto f=record(false);auto e=decode(f.data(),f.size());assert(e.name=="a.txt"&&e.logical==10000&&e.allocated==4096&&e.inode==1234&&e.links==2);
    auto d=record(true);e=decode(d.data(),d.size());assert(e.type==2&&e.name=="a.txt"&&e.logical==-1);
    auto err=record(false,true);e=decode(err.data(),err.size());assert(e.error==13&&e.name.empty());
    // Four-byte aligned 64-bit fields must work even at an odd buffer address.
    auto shifted=f;shifted.insert(shifted.begin(),0);assert(decode(shifted.data()+1,f.size()).inode==1234);
    for(size_t n=0;n<f.size();++n)must_throw([&]{(void)decode(f.data(),n);});
    auto corrupt=f;put(corrupt,28,int32_t(-100));must_throw([&]{decode(corrupt.data(),corrupt.size());});
    corrupt=f;put(corrupt,28,int32_t(1000000));must_throw([&]{decode(corrupt.data(),corrupt.size());});
    corrupt=f;put(corrupt,8,uint32_t(1));must_throw([&]{decode(corrupt.data(),corrupt.size());});
    std::vector<Totals> totals{{1,2,1,0,0},{3,4,1,0,0},{5,6,1,1,0},{7,8,1,0,1}};
    aggregate(totals,{0,0,0,1});assert(totals[0].logical==16&&totals[0].allocated==20&&totals[0].files==4&&totals[0].errors==1&&totals[0].excluded==1);
    assert(totals[1].logical==10);must_throw([&]{aggregate(totals,{0,1,0,1});});
    must_throw([]{add(UINT64_MAX,1);});
    TopK top(3,true);top.offer({999,1,1,1,"z"});top.offer({10,20,2,1,"c"});top.offer({5,20,3,1,"a"});top.offer({1,30,4,1,"b"});
    auto rows=top.sorted();assert(rows.size()==3&&rows[0].path=="b"&&rows[1].path=="a"&&rows[2].path=="c");
    assert(json_string("a\n\t\"\\\033")=="\"a\\u000a\\u0009\\\"\\\\\\u001b\"");
    // Parser fuzz smoke test: only bounded reads; arbitrary data may parse or throw.
    std::mt19937 rng(12345);
    for(int i=0;i<30000;++i){auto bytes=f;for(int j=0;j<3;++j)bytes[rng()%bytes.size()]=static_cast<unsigned char>(rng());try{(void)decode(bytes.data(),bytes.size());}catch(const std::exception&){} }
    std::cout<<"Core tests passed (decoder, malformed buffers, aggregation, top-K, overflow, escaping, 30,000 mutations).\n";
}

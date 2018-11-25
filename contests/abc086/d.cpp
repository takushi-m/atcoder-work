#include<iostream>
#include<vector>
using namespace std;

struct p {
  int x;
  int y;
};
vector<p> l;

int count(int x,int y,int K){
  int ret = 0;
  for(p v:l){
    int xx = (v.x-x+2*K)%(2*K);
    int yy = (v.y-y+2*K)%(2*K);
    if(xx<K && yy<K){
      ret++;
    }else if(xx>=K && yy>=K){
      ret++;
    }
  }
  return ret;
}

int main(){
  int N,K;
  cin>>N>>K;

  for(int i=0;i<N;++i){
    int x,y;
    string c;
    cin>>x>>y>>c;
    if(c=="W"){
      x += K;
    }
    p v;
    v.x = x%(2*K);
    v.y = y%(2*K);
    l.push_back(v);
  }

  int ret = -1;
  for(int x=0;x<2*K;++x){
    for(int y=0;y<=2*K;++y){
      int t = count(x,y,K);
      if(t>=ret){
        ret = t;
      }
    }
  }
  cout<<ret<<endl;
  return 0;
}

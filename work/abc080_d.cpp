#include<iostream>
#include<vector>
using namespace std;

int main(){
  int N,C;
  cin>>N>>C;
  int T = 0;
  vector<int> s(N);
  vector<int> t(N);
  vector<int> c(N);
  for(int i=0;i<N;++i){
    cin>>s[i]>>t[i]>>c[i];
    if(t[i]>T){
      T = t[i];
    }
  }

  vector<int> rm(2*T,0);
  for(int ci=0;ci<C;++ci){
    vector<int> tt(2*N,0);
    for(int i=0;i<N;++i){
      if(c[i]==ci+1){
        tt[2*s[i]-2] += 1;
        tt[2*t[i]-1] -= 1;
      }
    }
    for(int ti=0;ti<2*T-1;++ti){
      tt[ti+1] = tt[ti+1]+tt[ti];
    }
    for(int ti=0;ti<2*T;++ti){
      if(tt[ti]>0){
        rm[ti] += 1;
      }
    }
  }
  int ret = 0;
  for(int i=0;i<2*T;++i){
    if(ret<rm[i]){
      ret = rm[i];
    }
  }
  cout<<ret<<endl;
}

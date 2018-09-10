#include<iostream>
#include<algorithm>
using namespace std;

int main() {
  int n,m,r;
  cin>>n>>m>>r;
  int rr[8];
  for(int i=0;i<r;++i) {
    cin>>rr[i];
  }
  sort(rr,rr+r);

  int d[201][201];
  for(int i=0;i<201;++i){
    d[i][i] = 0;
    for(int j=0;j<201;++j){
      d[i][j] = 10^7;
    }
  }
  for(int i=0;i<m;++i) {
    int a,b,c;
    cin>>a>>b>>c;
    d[a][b] = c;
    d[b][a] = c;
  }

  for(int k=1;k<n+1;++k){
    for(int i=1;i<n+1;++i){
      for(int j=1;j<n+1;++j){
        if(d[i][k]+d[k][j]<d[i][j]){
          d[i][j] = d[i][k]+d[k][j];
        }
      }
    }
  }

  int ret = 10^7;
  do{
    int tmp = 0;
    for(int i=0;i<r-1;++i){
      tmp += d[rr[i]][rr[i+1]];
    }
    if(tmp<ret){
      ret = tmp;
    }
  }while(next_permutation(rr,rr+r));
  cout<<ret<<endl;

  return 0;
}

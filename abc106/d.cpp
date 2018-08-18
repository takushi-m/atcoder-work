#include<iostream>
#include<vector>
using namespace std;

int main() {
  int N,M,Q;
  cin>>N>>M>>Q;
  vector<vector<int> > memo = vector<vector<int> >(N+1, vector<int>(N+1, 0));
  for(int i=0;i<M;++i) {
    int x,y;
    cin>>x>>y;
    memo[x][y] += 1;
  }

  for(int i=0;i<Q;++i) {
    int p,q;
    cin>>p>>q;

    int ret = 0;
    for(int i=p;i<=q;++i) {
      for (int j=i;j<=q;++j) {
        ret += memo[i][j];
      }
    }
    cout<<ret<<endl;
  }
  return 0;
}

#include<iostream>
#include<vector>
using namespace std;

int main(){
  int n,m;
  cin>>n>>m;

  vector<vector<int>> edge(n);
  vector<int> iny = vector<int>(n,0);
  for(int i=0;i<m;i++){
    int x,y;
    cin>>x>>y;
    x -= 1;
    y -= 1;
    edge[x].push_back(y);
    iny[y]++;
  }

  vector<int> d = vector<int>(n, 0);

  for(int i=0;i<n;i++){
    if(d[i]>0 || iny[i]>0){
      continue;
    }
    vector<int> st = {i};
    while(st.size()>0){
      int s = st.back();
      st.pop_back();
      for(int j=0;j<edge[s].size();j++){
        int v = edge[s][j];
        if(d[v]<d[s]+1){
          d[v] = d[s]+1;
          st.push_back(v);
        }
      }
    }
  }

  int res = 0;
  for(int i=0;i<d.size();i++){
    res = max(res, d[i]);
  }
  cout<<res<<endl;
  return 0;
}

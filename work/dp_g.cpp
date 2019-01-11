#include<iostream>
#include<vector>
#include<queue>
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
  queue<int> st;
  for(int i=0;i<n;i++){
    if(iny[i]==0){
      st.push(i);
    }
  }

  while(st.size()>0){
    int s = st.front();
    st.pop();
    for(int j=0;j<edge[s].size();j++){
      int v = edge[s][j];
      if(iny[v]>0){
        iny[v]--;
      }
      if(iny[v]==0){
        d[v] = max(d[v], d[s]+1);
        st.push(v);
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

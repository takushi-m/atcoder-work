#include<iostream>
#include<vector>
#include<set>
using namespace std;

int main(){
  int n;
  cin>>n;
  int a[200000];
  int ia[200000];
  for(int i=0;i<n;++i){
    cin>>a[i];
    a[i]--;
    ia[a[i]] = i;
  }

  set<int> s;
  s.insert(-1);
  s.insert(n);
  long long ans = 0;
  for(int v=0;v<n;++v){
    auto it = s.lower_bound(ia[v]);
    int r = (*it);
    it--;
    int l = (*it);
    ans += (long long)(r-ia[v])*(ia[v]-l)*(v+1);
    s.insert(ia[v]);
  }
  cout<<ans<<endl;
}

#include<iostream>
#include<vector>
using namespace std;

typedef long long ll;

int main(){
  ll n;
  cin>>n;
  vector<vector<ll>> d = vector<vector<ll>>(n, vector<ll>(n,0));
  for(ll i=0;i<n;++i){
    for(ll j=0;j<n;++j){
      cin>>d[i][j];
    }
  }
  for(ll k=0;k<n;++k){
    for(ll i=0;i<n;++i){
      for(ll j=0;j<n;++j){
        if (d[i][j]>d[i][k]+d[k][j]){
          cout<<-1<<endl;
          return 0;
        }
      }
    }
  }
  ll res = 0;
  for(ll i=0;i<n;++i){
    for(ll j=i+1;j<n;++j){
      bool flag = true;
      for(ll k=0;k<n;++k){
        if(i==k || j==k){
          continue;
        }
        if(d[i][j]==d[i][k]+d[k][j]){
          flag = false;
          break;
        }
      }
      if(flag){
        res += d[i][j];
      }
    }
  }
  cout<<res<<endl;
}

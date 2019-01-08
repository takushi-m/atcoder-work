#include<iostream>
#include<iomanip>
#include<vector>
#include<algorithm>
#include<string>
using namespace std;

typedef long long ll;

int main(){
  ll n,W;
  cin>>n>>W;
  vector<ll> wl = vector<ll>(n);
  vector<ll> vl = vector<ll>(n);

  for(int i=0;i<n;i++){
    ll w,v;
    cin>>w>>v;
    wl[i] = w;
    vl[i] = v;
  }

  ll INF = 1000000000*n+10;
  ll V = 1000*n+10;
  vector<vector<ll>> dp = vector<vector<ll>>(n+1, vector<ll>(V+1, INF));
  dp[0][0] = 0;
  for(int vi=0;vi<V+1;vi++){
    for(int i=0;i<n;i++){
      if(vl[i]>vi){
        dp[i+1][vi] = dp[i][vi];
      }else{
        dp[i+1][vi] = min(dp[i][vi], dp[i][vi-vl[i]]+wl[i]);
      }
    }
  }

  ll res = 0;
  for(ll vi=0;vi<V+1;vi++){
    if(dp[n][vi]<=W){
      res = max(res, vi);
    }
  }
  cout<<res<<endl;
  return 0;
}

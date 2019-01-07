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

  vector<vector<ll>> dp = vector<vector<ll>>(n+1, vector<ll>(W+1, 0));
  for(int wi=1;wi<W+1;wi++){
    for(int i=0;i<n;i++){
      if(wl[i]>wi){
        dp[i+1][wi] = dp[i][wi];
      }else{
        dp[i+1][wi] = max(dp[i][wi], dp[i][wi-wl[i]]+vl[i]);
      }
    }
  }


  cout<<dp[n][W]<<endl;
  return 0;
}

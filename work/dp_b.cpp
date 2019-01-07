#include<iostream>
#include<iomanip>
#include<vector>
#include<algorithm>
#include<string>
using namespace std;

typedef long long ll;
ll INF = 1000000010;
int main(){
  ll n,k;
  cin>>n>>k;
  vector<ll> hl = vector<ll>(n);

  for(int i=0;i<n;i++){
    ll h;
    cin>>h;
    hl[i] = h;
  }

  vector<ll> dp = vector<ll>(n,INF);
  dp[0] = 0;
  for(int i=0;i<n;i++){
    for(int ki=1;ki<k+1;ki++){
      if(i+ki>n-1){
        break;
      }
      dp[i+ki] = min(dp[i+ki], dp[i]+abs(hl[i+ki]-hl[i]));
    }
  }
  cout<<dp[n-1]<<endl;
  return 0;
}

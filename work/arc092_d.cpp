#include<iostream>
#include<algorithm>
using namespace std;

typedef long long ll;

int main(){
  ll n;
  ll a[200000],b[200000];

  cin>>n;
  for(int i=0;i<n;++i){
    cin>>a[i];
  }
  for(int i=0;i<n;++i){
    cin>>b[i];
  }

  ll res = 0;
  for(int k=29;k>=0;--k){
    for(int i=0;i<n;++i){
      a[i] %= 1<<(k+1);
      b[i] %= 1<<(k+1);
    }
    sort(b,b+n);

    ll z = 0;
    for(int i=0;i<n;++i){
      z += lower_bound(b,b+n,2*(1<<k)-a[i]) - lower_bound(b,b+n,(1<<k)-a[i]);
      z += lower_bound(b,b+n,4*(1<<k)-a[i]) - lower_bound(b,b+n,3*(1<<k)-a[i]);
    }
    if(z%2==1){
      res += 1<<k;
    }
  }
  cout<<res<<endl;
}

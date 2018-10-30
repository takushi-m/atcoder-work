#include<iostream>
#include<cmath>
using namespace std;

typedef long long ll;


ll f(ll b, ll n){
  ll ret = 0;
  while(n>=b){
    ret += n%b;
    n = n/b;
  }
  return ret+n;
}

int main(){
  ll n,s;
  cin>>n>>s;
  if(s==n){
    cout<<n+1<<endl;
    return 0;
  }

  ll b=2;
  while(b*b<=n){
    if(f(b,n)==s){
      cout<<b<<endl;
      return 0;
    }
    b += 1;
  }

  ll p = ll(sqrt(n))+2;
  while(p>0){
    ll q = s - p;
    ll b = (n-q)/p;
    if(b>1 && f(b,n)==s){
      cout<<b<<endl;
      return 0;
    }
    p--;
  }

  cout<<-1<<endl;
  return 0;
}

#include<iostream>
#include<vector>
#include<string>
#include<map>
using namespace std;

int n;
string s;
vector<long long> hash1,power1,hash2,power2;

int base1 = 1007, mod1 = 1000000007;
int base2 = 2007, mod2 = 1000000009;

pair<long long, long long> get(int l, int r) {
  long long res1 = (hash1[r] - hash1[l]*power1[r-l]%mod1 + mod1) % mod1;
  long long res2 = (hash2[r] - hash2[l]*power2[r-l]%mod2 + mod2) % mod2;
  return {res1, res2};
}

bool check(int len) {
  map<pair<long long, long long>, int> d;
  for(int i=0;i+len<=n;i++) {
    auto h = get(i,i+len);
    if(d.count(h)>0){
      if(i-d[h]>=len) {
        return true;
      }
    } else {
      d[h] = i;
    }
  }
  return false;
}

int main() {
  cin>>n>>s;
  hash1.assign(n+1,0);
  hash2.assign(n+1,0);
  power1.assign(n+1,1);
  power2.assign(n+1,1);

  for(int i=0;i<n;i++) {
    hash1[i+1] = (hash1[i]*base1 + s[i])%mod1;
    power1[i+1] = (power1[i]*base1)%mod1;

    hash2[i+1] = (hash2[i]*base2 + s[i])%mod2;
    power2[i+1] = (power2[i]*base2)%mod2;
  }

  int ok = 0;
  int ng = n/2+1;
  while(ng-ok > 1) {
    int d = (ok+ng)>>1;
    if(check(d)){
      ok = d;
    } else {
      ng = d;
    }
  }

  cout<<ok<<endl;
}

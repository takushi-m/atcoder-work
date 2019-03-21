#include<iostream>
#include<iomanip>
#include<vector>
#include<algorithm>
#include<string>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;

void sample(){
  vector<vector<int>> vvi = vector<vector<int>>(20, vector<int>(10, 0));  // vvi[20][10]
  vector<vector<vector<int>>> vvvi = vector<vector<vector<int>>>(30, vector<vector<int>>(20, vector<int>(10, 0)));  // vvvi[30][20][10]

  vector<int> v = {3,2,1};
  sort(v.begin(), v.end());
  do {
    // pass
  } while(next_permutation(v.begin(), v.end()));

  for(auto x: v){
    cout<<x<<endl;
  }

  double res = 10.0;
  cout << fixed << setprecision(10) << res << endl;
}

int main(){
  ull MOD = 1000000007;
  int t;
  cin>>t;
  vector<int> al = vector<int>(400,0);
  for(int i=0;i<t;i++){
    cin>>al[i];
  }

  vector<vector<ull>> dp = vector<vector<ull>>(400, vector<ull>(700,0));
  ull res = 0;
  dp[0][0] = 1;
  for(int i=0;i<t;i++){
    for(int j=0;j<330;j++){
      for(int k=0;k<=al[i];k++){
        dp[i+1][j+k] += dp[i][2*j];
        dp[i+1][j+k] %= MOD;
      }
    }
    res += dp[i+1][1];
    res %= MOD;
  }
  for(int i=2;i<700;i*=2){
    res += dp[t][i];
    res %= MOD;
  }
  cout<<res<<endl;
}

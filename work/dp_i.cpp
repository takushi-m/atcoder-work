#include<iostream>
#include<iomanip>
#include<vector>
using namespace std;

int main(){
  int n;
  cin>>n;
  vector<double> p(n);
  for(int i=0;i<n;i++){
    cin>>p[i];
  }

  vector<vector<double>> dp =
    vector<vector<double>>(n+1, vector<double>(n+1, 0.0));
  dp[0][0] = 1.0;

  for(int i=0;i<n;i++){
    for(int j=0;j<=i;j++){
      dp[i+1][j+1] += dp[i][j]*p[i];
      dp[i+1][j] += dp[i][j]*(1-p[i]);
    }
  }

  double res = 0.0;
  for(int j=n;j>n/2;j--){
    res += dp[n][j];
  }

  cout << fixed << setprecision(10) << res << endl;
}

#include<iostream>
#include<vector>
using namespace std;

int main(){
  int n;
  cin>>n;
  vector<int> l;
  int p6=1,p9=1;
  for(int i=1;i<8;i++){
      p6 *= 6;
      p9 *= 9;
      l.push_back(p6);
      l.push_back(p9);
  }
  vector<int> dp;
  for(int i=0;i<n+1;i++){
    dp.push_back(i);
  }
  for(int i=0;i<l.size();i++){
    int x = l[i];
    if(x>n){
      continue;
    }
    for(int j=0;j<n-x+1;j++){
      dp[j+x] = min(dp[j+x], dp[j]+1);
    }
  }
  cout<<dp[n]<<endl;
}

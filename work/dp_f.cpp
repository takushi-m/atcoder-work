#include<iostream>
#include<string>
#include<vector>
using namespace std;

int main(){
  string s,t;
  cin>>s>>t;
  int ns = s.length();
  int nt = t.length();

  vector<vector<int>> dp =
    vector<vector<int>>(nt+1, vector<int>(ns+1,0));

  for(int ti=0;ti<nt;ti++){
    for(int si=0;si<ns;si++){
      int add = 0;
      if(t[ti]==s[si]){
        add = 1;
      }

      dp[ti+1][si+1] = max(
        dp[ti][si]+add,
        max(
          dp[ti+1][si],
          dp[ti][si+1]
        )
      );
    }
  }

  string res = "";
  int ti = nt;
  int si = ns;
  while(ti>0 && si>0){
    if(t[ti-1]==s[si-1]){
      res = s[si-1]+res;
      si -= 1;
      ti -= 1;
    }else if(dp[ti][si-1]>dp[ti-1][si]){
      si -= 1;
    }else{
      ti -= 1;
    }
  }

  cout<<res<<endl;
  return 0;
}

#include<iostream>
#include<iomanip>
#include<vector>
#include<algorithm>
#include<string>
#include<map>
using namespace std;

int main(){
  int n;
  string s;
  cin>>n>>s;
  int res = 0;
  map<string,int,less<>> d;


  for(int l1=0;l1<n;l1++){
    int m = l1+n/2+1;
    if(m>n){
      m = n;
    }
    for(int l2=m;l2>=l1+(res+1);l2--){
      string ss = s.substr(l1,l2-l1);
      auto at = d.find(ss);
      if(at==d.end()){
        d[ss] = l1;
      }else{
        int len = ss.length();
        if(d.at(ss)+len<=l1){
          if(res<len){
            res = len;
          }
        }
      }
    }
  }

  cout<<res<<endl;
}

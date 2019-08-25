#include<iostream>
#include<string>
using namespace std;

int main(){
  string s,t;
  cin>>s>>t;

  long long n = s.length();
  long long m = t.length();
  long long cnt = 0;
  for(int i=0;i<m;i++){
    int c = 0;
    while(c<n && s[cnt%n]!=t[i]) {
      cnt++;
      c++;
    }
    if (c==n) {
      cout<<-1<<endl;
      return 0;
    }
    cnt++;
  }
  cout<<cnt<<endl;
  return 0;
}

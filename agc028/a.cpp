#include<iostream>
#include<string>
using namespace std;

int gcd(int a,int b){
  if(a<b){
    int tmp = a;
    a = b;
    b = tmp;
  }
  if(b==0){
    return a;
  }
  int c = a%b;
  return gcd(b,c);
}

int lcm(int a,int b){
  return a*b/gcd(a,b);
}

int main(){
  int n,m;
  cin>>n>>m;
  string s,t;
  cin>>s;
  cin>>t;

  int l = lcm(n,m);
  string ls(l,'.');
  for(int i=0;i<n;++i){
    ls[i*l/n] = s[i];
  }
  for(int i=0;i<m;++i){
    if(ls[i*l/m]!='.' && ls[i*l/m]!=t[i]){
      cout<<-1<<endl;
      return 0;
    }
  }
  cout<<l<<endl;
  return 0;
}

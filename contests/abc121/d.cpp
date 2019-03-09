#include<iostream>
using namespace std;

int main(){
  unsigned long long a,b;
  cin>>a>>b;
  unsigned long long res = 0;
  for(unsigned long long i=a;i<=b;i++){
    res = res^i;
  }
  cout<<res<<endl;
}

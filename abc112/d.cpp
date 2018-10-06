#include<iostream>
using namespace std;

int main(){
  long long n,m;
  cin>>n>>m;

  long long maxg = m/n + 1;
  for(long long x=maxg;x>0;x--){
    if((m-x*(n-1))>0 && (m-x*(n-1))%x==0){
      cout<<x<<endl;
      return 0;
    }
  }
}

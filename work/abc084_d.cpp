#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main(){
  int Q;
  cin>>Q;
  int rmax;
  vector<int> qr(Q);
  vector<int> ql(Q);
  for(int i=0;i<Q;i++){
    cin>>ql[i]>>qr[i];
    if(qr[i]>rmax){
      rmax = qr[i];
    }
  }

  vector<int> prime;
  prime.push_back(2);
  for(int x=3;x<rmax+1;x++){
    bool pflag = true;
    for(auto n: prime){
      if(x%n==0){
        pflag = false;
        break;
      }
      if(x<n*n){
        break;
      }
    }
    if(pflag){
      prime.push_back(x);
    }
  }

  vector<int> acc(rmax+1, 0);
  for(int n=0;n<rmax+1;n++){
    if(find(prime.begin(),prime.end(),n)!=prime.end()
      && find(prime.begin(),prime.end(), (n+1)/2)!=prime.end()){
      acc[n] += 1;
    }
    if(n<rmax){
      acc[n+1] += acc[n];
    }
  }

  // for(auto x: prime){
  //   cout<<x<<" ";
  // }
  // cout<<endl;
  // for(auto x: acc){
  //   cout<<x<<" ";
  // }
  // cout<<endl;
  for(int i=0;i<Q;i++){
    cout<<acc[qr[i]]-acc[ql[i]-1]<<endl;
  }
}

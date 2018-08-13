#include<iostream>
using namespace std;

int main() {
  int n,k;
  cin>>n>>k;

  int ret = 0;
  for (int a=1;a<=n;a++) {
    if (a<k) {
      continue;
    }

    ret += n-a;
    if (k==0) {
      ret++;
    }
    if (k+1<=a/2) {
      ret += (a-k) - a/2;
      for (int b=k+1;b<a/2;b++) {
        if (a%b>=k) {
          ret++;
        }
      }
    } else {
      int t =  (a-k) - a/2;
      if (a%2==0) {
        t--;
      }
      if (t>=0) {
        ret += t;
      }
    }
  }
  cout<<ret<<endl;
  return 0;
}

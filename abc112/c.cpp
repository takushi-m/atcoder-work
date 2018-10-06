#include<iostream>
#include<vector>
using namespace std;

int main(){
  int n;
  cin>>n;
  vector<int> x(n);
  vector<int> y(n);
  vector<int> h(n);
  int maxh = -1;

  for(int i=0;i<n;++i){
    cin>>x[i]>>y[i]>>h[i];
    if(h[i]>maxh){
      maxh = h[i];
    }
  }

  for(int cx=0;cx<=100;++cx){
    for(int cy=0;cy<=100;++cy){
      for(int hi=maxh;hi<maxh+120;++hi){
        bool flag = true;
        for(int i=0;i<n;++i){
          int hh = max(hi-abs(cx-x[i])-abs(cy-y[i]), 0);
          if(h[i]!=hh){
            flag = false;
            break;
          }
        }
        if(flag){
          cout<<cx<<" "<<cy<<" "<<hi<<endl;
          return 0;
        }
      }
    }
  }
}

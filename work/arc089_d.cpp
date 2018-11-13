#include<iostream>
#include<vector>
using namespace std;

int main(){
  int n,k;
  cin>>n>>k;
  vector<vector<int>> d = vector<vector<int>>(2*k+1, vector<int>(2*k+1, 0));
  for(int i=0;i<n;++i){
    int x,y;
    char c;
    cin>>x>>y>>c;
    if(c=='B'){
      x += k;
    }
    x = x%(2*k);
    y = y%(2*k);
    cout<<"+"<<max(x-k+1,0)<<" "<<max(y-k+1,0)<<" "<<x<<" "<<y<<endl;
    d[max(x-k+1,0)][max(y-k+1,0)] += 1;
    d[x+1][y+1] += 1;
    d[max(x-k+1,0)][y+1] += -1;
    d[x+1][max(y-k+1,0)] += -1;
  }
    for(int hi=0;hi<2*k;++hi){
      for(int wi=0;wi<2*k;++wi){
        cout<<d[hi][wi]<<" ";
      }
      cout<<endl;
    }

  for(int hi=0;hi<2*k;++hi){
    for(int wi=0;wi<2*k;++wi){
      d[hi][wi+1] += d[hi][wi];
    }
  }
  for(int hi=0;hi<2*k;++hi){
    for(int wi=0;wi<2*k;++wi){
      d[hi+1][wi] += d[hi][wi];
    }
  }

  int res = 0;
  for(int hi=0;hi<2*k;++hi){
    for(int wi=0;wi<2*k;++wi){
      res = max(res, d[hi][wi]);
    }
  }
  cout<<res<<endl;
}

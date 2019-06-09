#include<iostream>
#include<iomanip>
#include<vector>
#include<algorithm>
#include<string>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;

int main(){
  int h,w;
  cin>>h>>w;
  vector<string> sl = vector<string>(h);
  for(int i=0;i<h;i++){
    cin>>sl[i];
  }

  vector<vector<vector<int>>> cnt = vector<vector<vector<int>>>(2010, vector<vector<int>>(2010, vector<int>(2, 0)));  // vvvi[30][20][10]

  for(int hi=0;hi<h;hi++){
    int wi = 0;
    while(wi<w){
      if(sl[hi][wi]=='.'){
        int c = 0;
        int wj = wi;
        while(wj<w && sl[hi][wj]=='.'){
          c += 1;
          wj += 1;
        }
        for(int j=wi;j<wj;j++){
          cnt[hi][j][0] = c;
        }
        wi = wj;
      }else{
        wi += 1;
      }
    }
  }

  for(int wi=0;wi<w;wi++){
    int hi = 0;
    while(hi<h){
      if(sl[hi][wi]=='.'){
        int c = 0;
        int hj = hi;
        while(hj<h && sl[hj][wi]=='.'){
          c += 1;
          hj += 1;
        }
        for(int j=hi;j<hj;j++){
          cnt[j][wi][1] = c;
        }
        hi = hj;
      }else{
        hi += 1;
      }
    }
  }

  int res = -1;
  for(int hi=0;hi<h;hi++){
    for(int wi=0;wi<w;wi++){
      if(sl[hi][wi]=='.'){
        int r = cnt[hi][wi][0]+cnt[hi][wi][1];
        if(r>res){
          res = r;
        }
      }
    }
  }
  cout<<res-1<<endl;
  return 0;
}

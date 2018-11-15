#include<iostream>
#include<vector>
using namespace std;

int main(){
  int n,k;
  cin>>n>>k;
  vector<vector<int>> d = vector<vector<int>>(4*k+1, vector<int>(4*k+1, 0));
  for(int i=0;i<n;++i){
    int x,y;
    char c;
    cin>>x>>y>>c;
    if(c=='B'){
      x += k;
    }
    x = x%(2*k);
    y = y%(2*k);
    d[max(y-k+1,0)][max(x-k+1,0)] += 1;
    d[y+1][x+1] += 1;
    d[y+1][max(x-k+1,0)] += -1;
    d[max(y-k+1,0)][x+1] += -1;

    int xs = (x+k)%(4*k);
    int ys = (y+k)%(4*k);
    d[max(ys-k+1,0)][max(xs-k+1,0)] += 1;
    d[ys+1][xs+1] += 1;
    d[ys+1][max(xs-k+1,0)] += -1;
    d[max(ys-k+1,0)][xs+1] += -1;

    xs = (x+2*k)%(4*k);
    ys = (y+2*k)%(4*k);
    d[max(ys-k+1,0)][max(xs-k+1,0)] += 1;
    d[ys+1][xs+1] += 1;
    d[ys+1][max(xs-k+1,0)] += -1;
    d[max(ys-k+1,0)][xs+1] += -1;

    xs = (x+3*k)%(4*k);
    ys = (y+3*k)%(4*k);
    d[max(ys-k+1,0)][max(xs-k+1,0)] += 1;
    d[ys+1][xs+1] += 1;
    d[ys+1][max(xs-k+1,0)] += -1;
    d[max(ys-k+1,0)][xs+1] += -1;

    xs = (x)%(4*k);
    ys = (y+2*k)%(4*k);
    d[max(ys-k+1,0)][max(xs-k+1,0)] += 1;
    d[ys+1][xs+1] += 1;
    d[ys+1][max(xs-k+1,0)] += -1;
    d[max(ys-k+1,0)][xs+1] += -1;

    xs = (x+2*k)%(4*k);
    ys = (y)%(4*k);
    d[max(ys-k+1,0)][max(xs-k+1,0)] += 1;
    d[ys+1][xs+1] += 1;
    d[ys+1][max(xs-k+1,0)] += -1;
    d[max(ys-k+1,0)][xs+1] += -1;

    xs = (x+k)%(4*k);
    ys = (y+3*k)%(4*k);
    d[max(ys-k+1,0)][max(xs-k+1,0)] += 1;
    d[ys+1][xs+1] += 1;
    d[ys+1][max(xs-k+1,0)] += -1;
    d[max(ys-k+1,0)][xs+1] += -1;

    xs = (x+3*k)%(4*k);
    ys = (y+k)%(4*k);
    d[max(ys-k+1,0)][max(xs-k+1,0)] += 1;
    d[ys+1][xs+1] += 1;
    d[ys+1][max(xs-k+1,0)] += -1;
    d[max(ys-k+1,0)][xs+1] += -1;
  }

  for(int hi=0;hi<4*k;++hi){
    for(int wi=0;wi<4*k;++wi){
      d[hi][wi+1] += d[hi][wi];
    }
  }
  for(int hi=0;hi<4*k;++hi){
    for(int wi=0;wi<4*k;++wi){
      d[hi+1][wi] += d[hi][wi];
    }
  }

  int res = 0;
  for(int hi=0;hi<4*k;++hi){
    for(int wi=0;wi<4*k;++wi){
      res = max(res, d[hi][wi]);
    }
  }
  cout<<res<<endl;
}

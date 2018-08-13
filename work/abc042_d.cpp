#include <iostream>
#include <vector>
using namespace std;

using ull = unsigned long long;

vector<ull> g,g2;
ull x = 1;

ull pow(ull a, ull n){
  if(n==0){
    return 1;
  }else if(n==1){
    return a;
  }else if(n%2==0){
    ull t = pow(a, n/2);
    return (t*t)%x;
  }else{
    return (a*pow(a, n-1))%x;
  }
}

ull route(int _h, int _w){
  int h = _h-1;
  int w = _w-1;
  ull ret = 1;
  return (((g[h+w]*g2[h])%x)*g2[w])%x;
}

int main() {
  int H,W,A,B;
  cin>>H>>W>>A>>B;
  for(int i=0;i<9;++i){
    x *= 10;
  }
  x += 7;

  g.push_back(1);
  g.push_back(1);
  g2.push_back(1);
  g2.push_back(1);

  for(int i=2;i<=H+W;++i){
    g.push_back((g[i-1]*i)%x);
    g2.push_back(pow(g[i], x-2));
    // cout<<g[i]<<" "<<g2[i]<<endl;
  }

  ull ret = 0;
  for(int h=1;h<H-A+1;++h){
    ull tmp = route(h, B);
    tmp *= route(H-h+1, W-B);
    ret = (ret+tmp)%x;
  }
  cout<<ret;
}

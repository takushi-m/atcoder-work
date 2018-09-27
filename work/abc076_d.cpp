#include<iostream>
#include<iomanip>
#include<vector>
using namespace std;

int n;
vector<int> t;
vector<int> v;

double func(double l,double r,double v,double x){
  if(x<=l){
    return v+(l-x);
  }else if(l<x && x<r){
    return v;
  }else{
    return v+(x-r);
  }
}

double getv(double x){
  double ret = func(0,0,0,x);
  int tt = 0;
  for(int i=0;i<n;++i){
    ret = min(ret, func(tt,tt+t[i],v[i],x));
    tt += t[i];
  }
  ret = min(ret, func(tt,tt,0,x));
  return ret;
}

int main(){
  int T = 0;
  cin>>n;
  for(int i=0;i<n;++i){
    int tmp;
    cin>>tmp;
    T += tmp;
    t.push_back(tmp);
  }
  for(int i=0;i<n;++i){
    int tmp;
    cin>>tmp;
    v.push_back(tmp);
  }

  double ret = 0;
  for(int i=0;i<2*T;++i){
    double a1 = i*0.5;
    double a2 = (i+1)*0.5;
    double v1 = getv(a1);
    double v2 = getv(a2);
    ret += 0.5*0.5*(v1+v2);
  }
  cout<<fixed<<setprecision(15)<<ret<<endl;
}

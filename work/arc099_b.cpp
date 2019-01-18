#include<iostream>
using namespace std;

int S(int n){
  int res = 0;
  while(n>0){
    res += n%10;
    n = n/10;
  }
  return res;
}

bool cmp(int x,int y){
  return x*S(y)<=y*S(x);
}

bool check(int n){
  for(int m=n+1;m<10000000;m++){
    if(!cmp(n,m)){
      return false;
    }
  }
  return true;
}

int log10(int x){
  int res = -1;
  while(x>0){
    res += 1;
    x /= 10;
  }
  return res;
}

int main(){
  int before = 0;
  for(int n=1;n<10000;n++){
    if(check(n)){
      cout<<n<<" "<<n-before<<endl;
      before = n;
    }
  }
  cout<<"---"<<endl;
  int k= 100;
  int n = 1;
  int d = d;
  for(int i=0;i<k;i++){
    int x = n+d;
    int y = n+10*d;
    if(check(x)){
      cout<<x<<endl;
      n = x;
    }else{
      cout<<y<<endl;
      d *= 10;
      n = y;
    }

  }
}

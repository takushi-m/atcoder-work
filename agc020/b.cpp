#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main(){
  int K;
  cin>>K;

  vector<int> A;
  for(int i=0;i<K;++i){
    int a;
    cin>>a;
    A.push_back(a);
  }

  reverse(begin(A), end(A));

  vector<int> n;
  n.push_back(2);

  for(int a:A){
    vector<int> tmp;
    for(int t:n){
      if(t%a!=0){
        continue;
      }
      for(int i=t;i<t+a;++i){
        tmp.push_back(i);
      }
    }
    if(tmp.size()==0){
      cout<<"-1"<<endl;
      return 0;
    }
    // unique(begin(tmp), end(tmp));
    n.clear();
    for(int x: tmp){
      n.push_back(x);
    }
  }

  if(n.size()>0){
    int n1 = *min_element(begin(n), end(n));
    int n2 = *max_element(begin(n), end(n));
    cout<<n1<<" "<<n2<<endl;
  }else{
    cout<<"-1"<<endl;
  }
}

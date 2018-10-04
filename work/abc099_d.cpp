#include<iostream>
#include<vector>
using namespace std;

int N,C;
vector<vector<int>> D;
vector<vector<int>> c;

long long e(vector<int> conv){
  long long ret = 0;
  for(int i=0;i<N;i++){
    for(int j=0;j<N;j++){
      int r = (i+j)%3;
      ret += D[c[i][j]-1][conv[r]-1];
    }
  }
  return ret;
}

int main(){
  cin>>N>>C;
  D = vector<vector<int>>(C, vector<int>(C, 0));
  for(int i=0;i<C;i++){
    for(int j=0;j<C;++j){
      cin>>D[i][j];
    }
  }
  c = vector<vector<int>>(N, vector<int>(N, 0));
  for(int i=0;i<N;i++){
    for(int j=0;j<N;j++){
      cin>>c[i][j];
    }
  }

  long long ret = -1;
  for(int ci=1;ci<=C;ci++){
    for(int cj=1;cj<=C;cj++){
      if(ci==cj){
        continue;
      }
      for(int ck=1;ck<=C;ck++){
        if(ci==ck || cj==ck){
          continue;
        }
        vector<int> conv{ci,cj,ck};
        long long t = e(conv);
        // cout<<"t:"<<t<<endl;
        if(ret<0){
          ret = t;
        }
        if(t<ret){
          ret = t;
        }
      }
    }
  }
  cout<<ret<<endl;
}

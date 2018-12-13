#include<iostream>
#include<iomanip>
#include<vector>
#include<algorithm>
using namespace std;

typedef ll long long;
typedef ull unsigned long long;

void sample(){
  vector<vector<int>> vvi = vector<vector<int>>(20, vector<int>(10, 0));  // vvi[20][10]
  vector<vector<vector<int>>> vvvi = vector<vector<vector<int>>>(30, vector<vector<int>>(20, vector<int>(10, 0)));  // vvvi[30][20][10]

  vector<int> v = {3,2,1};
  sort(v.begin(), v.end());
  do {
    // pass
  } while(next_permutation(v.begin(), v.end()));
}

void main(){

}

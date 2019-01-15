#include<iostream>
#include<iomanip>
#include<vector>
#include<algorithm>
#include<string>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;

struct UnionFind {
    vector<int> par;

    UnionFind(int n) : par(n, -1) { }
    void init(int n) { par.assign(n, -1); }

    int find(int x) {
        if (par[x] < 0) return x;
        else return par[x] = find(par[x]);
    }

    bool same(int x, int y) {
        return find(x) == find(y);
    }

    bool unite(int x, int y) {
        x = find(x); y = find(y);
        if (x == y) return false;
        if (par[x] > par[y]) swap(x, y); // merge technique
        par[x] += par[y];
        par[y] = x;
        return true;
    }

    int size(int x) {
        return -par[find(x)];
    }
};

void sample(){
  vector<vector<int>> vvi = vector<vector<int>>(20, vector<int>(10, 0));  // vvi[20][10]
  vector<vector<vector<int>>> vvvi = vector<vector<vector<int>>>(30, vector<vector<int>>(20, vector<int>(10, 0)));  // vvvi[30][20][10]

  vector<int> v = {3,2,1};
  sort(v.begin(), v.end());
  do {
    // pass
  } while(next_permutation(v.begin(), v.end()));

  for(auto x: v){
    cout<<x<<endl;
  }

  double res = 10.0;
  cout << fixed << setprecision(10) << res << endl;
}

int main(){
  return 42;
}

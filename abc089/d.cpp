#include<iostream>
#include<vector>
#include<map>
#include<utility>
using namespace std;

vector<pair<int, int> > table(300*300+1);
map<string, int> cache;

int calc(int l, int r, int d) {
  if (l==r) {
    return 0;
  }

  string k = to_string(l)+"|"+to_string(r);
  if (cache.find(k) != cache.end()) {
    return cache[k];
  }
  int ret = abs(table[l].first - table[l+d].first) + abs(table[l].second - table[l+d].second) + calc(l+d,r,d);
  cache[k] = ret;
  return ret;
}

int main() {
  int h,w,d;
  cin>>h>>w>>d;

  for (int hi=0;hi<h;++hi) {
    for (int wi=0;wi<w;++wi) {
      int x;
      cin>>x;
      table[x] = make_pair(hi+1, wi+1);
    }
  }

  int q;
  cin>>q;
  for (int i=0;i<q;++i) {
    int l,r;
    cin>>l>>r;
    cout<<calc(l,r,d)<<endl;
  }
}

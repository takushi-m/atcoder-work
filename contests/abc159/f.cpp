#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>
using namespace std;

const int MAX = 1000;

void rec(const vector<vector<long long>> &dp, const vector<int> &a, int i, int j, deque<int> &keiro, vector<deque<int>> &ans) {
    if (i == 0) {
        if (j == 0) {
            ans.push_back(keiro);
        }
        return;
    }

    // 上へ遡る (dp[i-1][j] == 0) だったら無視)
    if (dp[i-1][j]) {
        rec(dp, a, i-1, j, keiro, ans);
    }
    // 左上へ遡る (dp[i-1][j-a[i-1]] == 0 だったら無視)
    if (j-a[i-1] >= 0 && dp[i-1][j-a[i-1]]) {
        keiro.push_front(i-1);
        rec(dp, a, i-1, j-a[i-1], keiro, ans);
        keiro.pop_front();
    }
}


int main() {
    int N, X;
    cin >> N >> X;
    vector<int> a(N);
    for (int i = 0; i < N; ++i) cin >> a[i];

    // DP
    vector<vector<long long>> dp(N+1, vector<long long>(MAX, 0));
    dp[0][0] = 1;
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < MAX; ++j) {
            dp[i+1][j] += dp[i][j];
            if (j + a[i] < MAX) dp[i+1][j+a[i]] += dp[i][j];
        }
    }

    // 復元
    deque<int> keiro;
    vector<deque<int>> ans;
    rec(dp, a, N, X, keiro, ans);

    // 出力
    int res = 0;
    int mod = 998244353;
    for (int i = 0; i < ans.size(); ++i) {
        int l=-1,r=-1;
        for (auto el : ans[i]) {
          if (l<0){
            l = el;
          }
          r = el;
        }
        res += (l+1)*(N-r);
        res = res%mod;
    }
    cout<<res<<endl;
}
#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>
using namespace std;

const long long MAX = 3010;

void rec(const vector<vector<long long>> &dp, const vector<long long> &a, int i, int j, deque<long long> &keiro, vector<deque<long long>> &ans) {
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
        keiro.push_front(a[i-1]);
        rec(dp, a, i-1, j-a[i-1], keiro, ans);
        keiro.pop_front();
    }
}

long long modpow(long long a, long long n, long long mod) {
    long long res = 1;
    while (n > 0) {
        if (n & 1) res = res * a % mod;
        a = a * a % mod;
        n >>= 1;
    }
    return res;
}

int main() {
    long long mod = 998244353;
    long long res = 0;
    long long N, X;
    cin >> N >> X;
    vector<long long> a(N);
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
    deque<long long> keiro;
    vector<deque<long long>> ans;
    rec(dp, a, N, X, keiro, ans);

    // 出力
    for (int i = 0; i < ans.size(); ++i) {
        res += modpow(2, N - ans[i].size(), mod);
        res %= mod;
    }
    cout<<res<<endl;
}
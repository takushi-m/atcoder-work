# -*- coding: utf-8 -*-

# 二分探索
### bisect.bisect_leftを使うことも検討する
def lower_bound(al, key):
    """
    一般に左側が満たしておらず、右側は満たしている判定基準(境目は一つ)ならlower_boundになる
    (条件を満たすもののうち、最小のインデックスを返す)
    単調にさえなっていれば、左右が逆になっていても検索には使える(ng/okも一緒に逆にする必要がある)
    """
    def isOk(a):
        # alの中でkey以上のアイテムのうち最小のインデックスを返す
        # upper_boundにする時にはa>key
        return a>=key

    ng = -1
    ok = len(al)

    while abs(ok-ng)>1:
        mid = (ok+ng)//2

        if isOk(al[mid]):
            ok = mid
        else:
            ng = mid

    return ok

# 最長増加部分列
def lis(al):
    n = len(al)
    dp = [10**9]*(n+1)

    for a in al:
        dp[lower_bound(dp, a)] = a
    return lower_bound(dp, 10**9)

n = int(input())
cl = [int(input()) for _ in range(n)]
print(n-lis(cl))
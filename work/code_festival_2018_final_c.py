# -*- coding: utf-8 -*-
n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]
ab.sort()
m = int(input())
tl = [int(input()) for _ in range(m)]

def cost(i,t):
    j = i - 1
    if t>=ab[i][0]:
        res1 = ab[i][1] + (t-ab[i][0])
    else:
        res1 = ab[i][1]

    if t>=ab[j][0]:
        res2 = ab[j][1] + (t-ab[j][0])
    else:
        res2 = ab[j][1]

    return min(res1,res2)

# 二分探索
def lower_bound(al, key):
    """
    一般に左側が満たしておらず、右側は満たしている判定基準(境目は一つ)ならlower_boundになる
    (条件を満たすもののうち、最小のインデックスを返す)
    単調にさえなっていれば、左右が逆になっていても検索には使える(ng/okも一緒に逆にする必要がある)
    """
    def isOk(a):
        # alの中でkey以上のアイテムのうち最小のインデックスを返す
        # upper_boundにする時にはa>key
        return a[0]>=key

    ng = -1
    ok = len(al)

    while abs(ok-ng)>1:
        mid = (ok+ng)//2

        if isOk(al[mid]):
            ok = mid
        else:
            ng = mid

    return ok

for t in tl:
    if t<=ab[0][0]:
        print(ab[0][1])
    elif t>=ab[n-1][0]:
        print(ab[n-1][1]+(t-ab[n-1][0]))
    else:
        i = lower_bound(ab, t)
        print(cost(i, t))

# -*- coding: utf-8 -*-
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

n,k = map(int, input().split())
al = list(map(int, input().split()))
bl = list(map(int, input().split()))
al.sort()
bl.sort()

def isOk(x):
    ai = 0
    res = 0
    while ai<n and al[ai]<=x:
        a = al[ai]
        b = x//a
        res += lower_bound(bl, b+1)
        ai += 1
    return res>=k

ng = -1
ok = 10**18+1

while ok-ng>1:
    mid = (ok+ng)//2

    if isOk(mid):
        ok = mid
    else:
        ng = mid

print(ok)

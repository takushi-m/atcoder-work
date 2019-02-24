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


a,b,q = map(int, input().split())
sl = [int(input()) for _ in range(a)]
tl = [int(input()) for _ in range(b)]
xl = [int(input()) for _ in range(q)]
# print(sl)
# print(tl)
for x in xl:
    si = lower_bound(sl,x)
    ti = lower_bound(tl,x)
    # print(x,si,ti)

    ssl = []
    if si==a:
        ssl.append(sl[-1])
    elif si==-1:
        ssl.append(sl[0])
    else:
        ssl.append(sl[si])
        if si>0:
            ssl.append(sl[si-1])
    ttl = []
    if ti==b:
        ttl.append(tl[-1])
    elif ti==-1:
        ttl.append(tl[0])
    else:
        ttl.append(tl[ti])
        if ti>0:
            ttl.append(tl[ti-1])

    res = -1
    for s in ssl:
        for t in ttl:
            if s>=x and t>=x:
                tmp = max(s-x, t-x)
            elif s<x and t<x:
                tmp = max(x-s, x-t)
            elif s>=x>=t:
                tmp = min(
                    2*(s-x)+(x-t),
                    (s-x)+2*(x-t)
                )
            else:
                tmp = min(
                    2*(x-s)+(t-x),
                    (x-s)+2*(t-x)
                )
            if res<0:
                res = tmp
            else:
                res = min(res,tmp)
    print(res)

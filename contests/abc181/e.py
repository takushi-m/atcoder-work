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

n,m = map(int, input().split())
hl = list(map(int, input().split()))
wl = list(map(int, input().split()))

hl.sort()
res = 10**15

acc1 = [0]*(n+1)
acc2 = [0]*(n+1)
for i in range(n-1):
    d = hl[i+1]-hl[i]
    if i%2==0:
        acc1[i+2] += acc1[i]+d
        acc1[i+1] = acc1[i]
    else:
        acc2[i+2] += acc2[i]+d
        acc2[i+1] = acc2[i]
if n%2==0:
    acc2[n] = acc2[n-1]
else:
    acc1[n] = acc1[n-1]

for w in wl:
    i = lower_bound(hl, w)
    if i<0:
        r1 = acc2[-1]
        res = min(res, r1+hl[0]-w)
    elif i==n:
        r1 = acc1[-1]
        res = min(res, r1+w-hl[-1])
    elif i%2==0:
        r1 = acc1[i]
        r2 = acc2[-1] - acc2[i+1]
        res = min(res, r1+r2+hl[i]-w)
    else:
        r1 = acc1[i-1]
        r2 = acc2[-1] - acc2[i]
        res = min(res, r1+r2+w-hl[i-1])
print(res)

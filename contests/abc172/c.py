def lower_bound(al, key):
    """
    一般に左側が満たしておらず、右側は満たしている判定基準(境目は一つ)ならlower_boundになる
    (条件を満たすもののうち、最小のインデックスを返す)
    単調にさえなっていれば、左右が逆になっていても検索には使える(ng/okも一緒に逆にする必要がある)
    """
    def isOk(a):
        # alの中でkey以上のアイテムのうち最小のインデックスを返す
        # upper_boundにする時にはa>key
        return a>key

    ng = -1
    ok = len(al)

    while abs(ok-ng)>1:
        mid = (ok+ng)//2

        if isOk(al[mid]):
            ok = mid
        else:
            ng = mid

    return ok

n,m,k = map(int, input().split())
al = list(map(int, input().split()))
bl = list(map(int, input().split()))

acc_a = [0]*(n+1)
acc_b = [0]*(m+1)
for i in range(n):
    acc_a[i+1] = acc_a[i] + al[i]
for i in range(m):
    acc_b[i+1] = acc_b[i] + bl[i]

res = 0

for i in range(n):
    s = acc_a[i+1]
    if s>k:
        continue
    j = lower_bound(acc_b, k-s)

    if j>=0:
        res = max(res, i+1 + j-1)

for i in range(m):
    s = acc_b[i+1]
    if s>k:
        continue
    j = lower_bound(acc_a, k-s)

    if j>=0:
        res = max(res, i+1 + j-1)

print(res)
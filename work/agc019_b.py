from string import ascii_lowercase
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

s = input()
n = len(s)

d = {}
for c in ascii_lowercase:
    d[c] = []

for i in range(n):
    d[s[i]].append(i)

res = 1
for i in range(n):
    c = s[i]
    j = lower_bound(d[c],i)
    res += (n-i) - (len(d[c])-j) - 1
print(res)
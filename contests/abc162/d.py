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

n = int(input())
s = list(input())

d = {"R":[],"G":[],"B":[]}

for i in range(n):
    d[s[i]].append(i)

res = 0
for i in range(n-2):
    for j in range(i+1,n-1):
        if s[i]==s[j]:
            continue
        if s[i]=="R":
            if s[j]=="G":
                k = "B"
            else:
                k = "G"
        elif s[i]=="G":
            if s[j]=="R":
                k = "B"
            else:
                k = "R"
        else:
            if s[j]=="G":
                k = "R"
            else:
                k = "G"
        
        x = lower_bound(d[k],j)
        if x<0 or x>=len(d[k]):
            continue
        ki = j + (j-i)
        res += len(d[k])-x
        if ki<n and s[ki]==k:
            if s[ki]==k:
                res -= 1
print(res)
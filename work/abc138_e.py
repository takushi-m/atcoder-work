# -*- coding: utf-8 -*-

def lower_bound(l,k):
    def isOk(i):
        return l[i]>k

    ok = len(l)
    ng = -1
    while abs(ok-ng) > 1:
        mid = (ok+ng)//2

        if isOk(mid):
            ok = mid
        else:
            ng = mid
    return ok

s = input()
n = len(s)
t = input()
m = len(t)

d = {}
for c in t:
    if c in d:
        continue
    else:
        d[c] = []
    for i in range(2*n):
        if s[i%n]==c:
            d[c].append(i)
res = -1
for i in range(m):
    c = t[i]
    if len(d[c])==0:
        print(-1)
        exit()

    j = lower_bound(d[c],res%n)
    res += d[c][j] - res%n

print(res+1)

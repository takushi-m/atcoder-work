# -*- coding: utf-8 -*-
n,q = map(int, input().split())
s = input()
td = [input().split() for _ in range(q)]

def check(idx, x):
    for t,d in td:
        if idx==x:
            return True
        elif idx==n or idx==-1:
            return False

        if s[idx]==t:
            if d=="L":
                idx -= 1
            else:
                idx += 1
    return idx==x

ok = -1
ng = n
while abs(ok-ng)>1:
    mid = (ok+ng)//2
    if check(mid, -1):
        ok = mid
    else:
        ng = mid
res = ok+1

ok = n
ng = -1
while abs(ok-ng)>1:
    mid = (ok+ng)//2
    if check(mid, n):
        ok = mid
    else:
        ng = mid
res += n-ok

print(n-res)

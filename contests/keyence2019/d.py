# -*- coding: utf-8 -*-
n,m = map(int, input().split())
al = list(map(int, input().split()))
sa = set(al)
bl = list(map(int, input().split()))
sb = set(bl)
al.sort()
bl.sort()

def counta(x):
    ng = -1
    ok = n
    while abs(ok-ng)>1:
        mid = (ok+ng)//2
        if al[mid]>=x:
            ok = mid
        else:
            ng = mid

    return n-ok


def countb(x):
    ng = -1
    ok = m
    while abs(ok-ng)>1:
        mid = (ok+ng)//2
        if bl[mid]>=x:
            ok = mid
        else:
            ng = mid

    return n-ok


res = 1
MOD = 10**9+7
s = 0
for i in range(n*m,0,-1):
    if i in sa:
        na = 1
    else:
        na = counta(i)
    if i in sb:
        nb = 1
    else:
        nb = countb(i)

    if na*nb==1:
        s += 1
        continue
    # print(i,na*nb,s)
    if na*nb-s<=0:
        print(0)
        exit()
    res *= (na*nb-s)
    res %= MOD
    s += 1

print(res)

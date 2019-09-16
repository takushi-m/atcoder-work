# -*- coding: utf-8 -*-

n = int(input())
s = input()

ok = 0
ng = n//2+1

while ng-ok>1:
    mid = (ok+ng)//2

    d = {}
    isOk = False
    for l in range(n-mid+1):
        ss = s[l:l+mid]
        if ss not in d:
            d[ss] = l
        else:
            l2 = d[ss]
            if l2+mid<=l:
                isOk = True
                break

    if isOk:
        ok = mid
    else:
        ng = mid

print(ok)

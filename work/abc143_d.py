# -*- coding: utf-8 -*-

def bsearch(l,n,k):
    ok = -1
    ng = n

    while ng-ok>1:
        mid = (ng+ok)//2
        if l[mid]<k:
            ok = mid
        else:
            ng = mid
    return ok

def f(l):
    n = len(l)
    l.sort()

    res = 0
    for i in range(n-1):
        for j in range(i+1,n):
            k = bsearch(l,n,l[i]+l[j])
            res += k-j

    return res

if __name__ == '__main__':
    n = int(input())
    l = list(map(int, input().split()))
    print(f(l))


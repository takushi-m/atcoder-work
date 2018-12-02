# -*- coding: utf-8 -*-
n,x = map(int, input().split())
xl = list(map(int, input().split()))

def gcd(a,b):
    if b>a:
        a,b = b,a
    while b!=0:
        a,b = b,a%b
    return a

xl.append(x)
xl.sort()
res = None
for i in range(n):
    d = xl[i+1] - xl[i]
    if res is None:
        res = d
    else:
        res = gcd(res, d)
print(res)

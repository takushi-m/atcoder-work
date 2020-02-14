# -*- coding: utf-8 -*-
from collections import defaultdict
def primeFactors(n):
    res = []
    while n%2==0:
        res.append(2)
        n //= 2
    x = 3
    while n>1 and n>=x*x:
        while n%x==0:
            res.append(x)
            n //= x
        x += 2
    if n>1:
        res.append(n)
    return res

def modpow(a,n,m):
    res = 1
    while n>0:
        if n%2==1:
            res = (res * a) % m
        a = (a*a) % m
        n = n//2
    return res

MOD = 10**9 + 7
n = int(input())
d = defaultdict(int)
for i in range(1,n+1):
    for r in primeFactors(i):
        d[r] += 1

res = 1
for k in d.keys():
    res *= (d[k]+1)
    res %= MOD
print(res)
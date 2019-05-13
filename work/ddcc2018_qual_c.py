# -*- coding: utf-8 -*-
MOD = 1000000007

def modpow(a,n,m):
    res = 1
    while n>0:
        if n%2==1:
            res = (res * a) % m
        a = (a*a) % m
        n = n//2
    return res

n = int(input())

res = 0
for c in range(1,n+1):
    r = (modpow(c,10,MOD) - modpow(c-1,10,MOD))%MOD
    if r<0:
        r += MOD

    res += r * modpow(n//c,10,MOD)
    res %= MOD

print(res)

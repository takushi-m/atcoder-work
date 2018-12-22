# -*- coding: utf-8 -*-
# s = list(input())
from random import randrange
s = [["A","B","C","?"][randrange(4)] for _ in range(10**5)]
n = len(s)
MOD = 10**9 + 7

memo = {}
def modpow(a,n,m):
    if n in memo:
        return memo[n]
    res = 1
    while n>0:
        if n%2==1:
            res = (res * a) % m
        a = (a*a) % m
        n = n//2
    memo[n] = res
    return res

al = [0]*(n+1)
bl = [0]*(n+1)
cl = [0]*(n+1)
ql = [0]*(n+1)
for i in range(n):
    if s[i]=="A":
        al[i+1] += 1
    elif s[i]=="B":
        bl[i+1] += 1
    elif s[i]=="C":
        cl[i+1] += 1
    else:
        ql[i+1] += 1

    al[i+1] += al[i]
    bl[i+1] += bl[i]
    cl[i+1] += cl[i]
    ql[i+1] += ql[i]

res = 0
for i in range(n):
    if s[i]=="A" or s[i]=="C":
        continue

    res += ((al[i]-al[0])*(cl[n]-cl[i+1])*modpow(3,(ql[i]-ql[0] + ql[n]-ql[i+1]),MOD))%MOD
    res %= MOD
    res += ((al[i]-al[0])*(ql[n]-ql[i+1])*modpow(3,(ql[i]-ql[0] + ql[n]-ql[i+1]-1),MOD))%MOD
    res %= MOD
    res += ((ql[i]-ql[0])*(cl[n]-cl[i+1])*modpow(3,(ql[i]-ql[0]-1 + ql[n]-ql[i+1]),MOD))%MOD
    res %= MOD
    res += ((ql[i]-ql[0])*(ql[n]-ql[i+1])*modpow(3,(ql[i]-ql[0]-1 + ql[n]-ql[i+1]-1),MOD))%MOD
    res %= MOD

print(res)

# -*- coding: utf-8 -*-
n = int(input())
al = list(map(int, input().split()))

def gcd(a,b):
    while b!=0:
        a,b = b,a%b
    return a

res = al[0]
for i in range(1,n):
    res = gcd(res,al[i])

print(res)

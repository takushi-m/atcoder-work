# -*- coding: utf-8 -*-
n = int(input())

def gcd(a,b):
    if b>a:
        a,b = b,a
    while b>0:
        a,b = b,a%b
    return a

def lcm(a,b):
    return a*b//gcd(a,b)

res = int(input())
for _ in range(n-1):
    t = int(input())
    res = lcm(res,t)

print(res)

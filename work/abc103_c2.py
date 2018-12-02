# -*- coding: utf-8 -*-
n = int(input())
al = list(map(int, input().split()))

def gcd(a,b):
    if b>a:
        a,b = b,a
    while b!=0:
        a,b = b,a%b
    return a

def lcm(a,b):
    return a*b//gcd(a,b)

def f(m):
    s = 0
    for i in range(n):
        s += m%al[i]
    return s

res = al[0]
for i in range(1,n):
    res = lcm(res,al[i])


print(f(res-1))

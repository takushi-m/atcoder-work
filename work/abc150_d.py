# -*- coding: utf-8 -*-
from functools import reduce
from math import ceil
# GCD
def gcd(a,b):
    while b!=0:
        a,b = b,a%b
    return a

# lのGCD
def lcmlist(l):
    res = l[0]
    for i in range(1,len(l)):
        g = gcd(res, l[i])
        res = res*l[i]//g
    return res


n,m = map(int, input().split())
al = list(map(int, input().split()))

l = []
c = 0
for i in range(n):
    l.append(al[i]//2)
    cc = 0
    while al[i]%2==0:
        al[i] //= 2
        cc += 1

    if c==0:
        c = cc
    else:
        if c!=cc:
            print(0)
            exit()

g = lcmlist(l)
# if g%2==1:
#     print(0)
#     exit()

x = m//g
if x%2==1:
    print((x-1)//2+1)
else:
    print(x//2)
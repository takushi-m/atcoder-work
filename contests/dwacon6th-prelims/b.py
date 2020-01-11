# -*- coding: utf-8 -*-

def fac(x):
    res = 1
    for i in range(1,x+1):
        res *= i
    return res

MOD = 10**9 + 7
n = int(input())
xl = list(map(int, input().split()))

res = 0
for i in range(n-1):
    res = res + (xl[i+1]-xl[i])*fac(i) + (res+xl[i+1]-xl[i])*fac(i)

print(res)
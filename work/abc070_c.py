# -*- coding: utf-8 -*-

n = int(input())

def gcd(a, b):
    if b==0:
        return a
    return gcd(b, a%b)

def lcm(a,b):
    return a//gcd(a,b)*b

ans = 1
for _ in range(n):
    t = int(input())
    ans = lcm(ans, t)

print(ans)

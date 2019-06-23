# -*- coding: utf-8 -*-
a,b,c,d = map(int, input().split())

def gcd(x,y):
    while y>0:
        x,y = y,x%y
    return x

x = c*d//gcd(c,d)
a -= 1
ans = b//c - a//c
ans += b//d - a//d
ans -= b//x - a//x

ans = b-a-ans
print(ans)

# -*- coding: utf-8 -*-
n,k = map(int, input().split())
a = list(map(int, input().split()))

def gcd(a,b):
    if a<b:
        a,b = b,a
    while b>0:
        a,b = b,a%b
    return a

g = a[0]
for i in range(1,n):
    g = gcd(g,a[i])

if max(a)>=k and k%g==0:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")

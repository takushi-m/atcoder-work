# -*- coding: utf-8 -*-
n = int(input())
al = list(map(int, input().split()))

def gcd(a,b):
    while b>0:
        a,b = b,a%b
    return a

ll = [0]*n
ll[0] = al[0]
for i in range(1,n):
    ll[i] = gcd(al[i], ll[i-1])

rl = [0]*n
rl[n-1] = al[n-1]
for i in range(n-2,-1,-1):
    rl[i] = gcd(al[i],rl[i+1])

res = -1

for i in range(n):
    if i==0:
        res = max(res, rl[1])
    elif i==n-1:
        res = max(res, ll[n-2])
    else:
        res = max(res, gcd(ll[i-1],rl[i+1]))

print(res)

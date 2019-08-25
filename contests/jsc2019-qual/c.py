# -*- coding: utf-8 -*-
MOD = 10**9+7

n = int(input())
s = input()

if s[0]=="W" or s[-1]=="W":
    print(0)
    exit()

lr = ["L"]
for i in range(1,2*n):
    if s[i-1]==s[i]:
        if lr[i-1]=="L":
            lr.append("R")
        else:
            lr.append("L")
    else:
        lr.append(lr[i-1])

la = [0 for _ in range(2*n+1)]
ra = [0 for _ in range(2*n+1)]
for i in range(2*n):
    if lr[i]=="L":
        la[i+1] = la[i]+1
        ra[i+1] = ra[i]
    else:
        la[i+1] = la[i]
        ra[i+1] = ra[i]+1
if la[-1]!=ra[-1]:
    print(0)
    exit()

res = 1
for i in range(2*n):
    if lr[i]=="R":
        res *= la[i]-ra[i]
        res %= MOD

for i in range(2,n+1):
    res = (res*i)%MOD

print(res)

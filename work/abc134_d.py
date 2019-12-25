# -*- coding: utf-8 -*-
n = int(input())
al = list(map(int, input().split()))

bl = [0]*n
for i in range(n,0,-1):
    if i*2>n:
        if al[i-1]>0:
            bl[i-1] = 1
        continue

    c = 2
    s = 0
    while i*c<=n:
        s += bl[i*c-1]
        c += 1
    if al[i-1]==1:
        bl[i-1] = 1 if s%2==0 else 0
    else:
        bl[i-1] = 0 if s%2==0 else 1

res = []
for i in range(1,n+1):
    if bl[i-1]>0:
        res.append(i)

print(len(res))
if len(res)>0:
    print(*res)
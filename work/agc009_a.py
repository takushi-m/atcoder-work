# -*- coding: utf-8 -*-
n = int(input())
ab = []
for _ in range(n):
    a,b = map(int, input().split())
    ab.append((a,b))

res = 0
for i in range(n-1,-1,-1):
    a,b = ab[i]
    a += res
    if b>=a>0:
        res += b-a
    elif a%b==0:
        pass
    else:
        res += b-a%b
print(res)

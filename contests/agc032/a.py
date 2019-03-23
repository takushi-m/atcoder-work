# -*- coding: utf-8 -*-
n = int(input())
bl = list(map(int, input().split()))

res = []
for i in range(n):
    b = bl[i]
    if i<b-1:
        print(-1)
        exit()
    res.insert(b-1,b)

for r in res:
    print(r)

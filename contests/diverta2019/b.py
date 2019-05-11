# -*- coding: utf-8 -*-
r,g,b,n = map(int, input().split())

cnt = 0
for ri in range(n+1):
    if r*ri>n:
        break
    for gi in range(n+1):
        x = n - r*ri - g*gi
        if x<0:
            break
        if x%b==0:
            cnt += 1

print(cnt)

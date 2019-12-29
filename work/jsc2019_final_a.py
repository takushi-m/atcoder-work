# -*- coding: utf-8 -*-
n,m = map(int, input().split())
al = list(map(int, input().split()))
bl = list(map(int, input().split()))

s = {}

for i in range(n):
    for j in range(m):
        a = al[i]
        b = bl[j]
        w = a+b
        if w in s:
            x,y = s[w]
            print(i,j,x,y)
            exit()
        s[w] = (i,j)

print(-1)
# -*- coding: utf-8 -*-
n,m = map(int, input().split())
ps = [input().split() for _ in range(m)]

wa = [0]*(n+1)
solve = [False for _ in range(n+1)]
for p,s in ps:
    p = int(p)
    if s=="AC":
        solve[p] = True
    else:
        if not solve[p]:
            wa[p] += 1

ra = 0
rw = 0
for i in range(1,n+1):
    if solve[i]:
        ra += 1
        rw += wa[i]
print(ra,rw)

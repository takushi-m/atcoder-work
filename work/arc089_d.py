# -*- coding: utf-8 -*-
n,k = map(int, input().split())

d = [[0 for _ in range(2*k+1)] for _ in range(2*k+1)]

for _ in range(n):
    x,y,c = input().split()
    x = int(x)
    y = int(y)
    if c=="B":
        x += k
    x %= 2*k
    y %= 2*k

    d[max(x-k,0)][max(y-k,0)] += 1
    d[x+1][y+1] += 1
    d[max(x-k,0)][y+1] += -1
    d[x+1][max(y-k,0)] += -1

for hi in range(2*k):
    for wi in range(2*k):
        d[hi][wi+1] += d[hi][wi]
for hi in range(2*k):
    for wi in range(2*k):
        d[hi+1][wi] += d[hi][wi]

res = 0
for hi in range(2*k):
    for wi in range(2*k):
        res = max(res, d[hi][wi])
print(res)

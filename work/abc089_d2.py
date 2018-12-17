# -*- coding: utf-8 -*-
h,w,d = map(int, input().split())
dd = {}
for hi in range(h):
    line = list(map(int, input().split()))
    for wi in range(w):
        dd[line[wi]] = (hi, wi)
q = int(input())
lr = [list(map(int, input().split())) for _ in range(q)]

acc = [0]*(h*w+1)
for i in range(h*w+1):
    if i<=d:
        acc[i] = 0
        continue

    h1,w1 = dd[i]
    h2,w2 = dd[i-d]
    acc[i] = acc[i-d] + abs(h1-h2) + abs(w1-w2)

for (l,r) in lr:
    print(acc[r] - acc[l])

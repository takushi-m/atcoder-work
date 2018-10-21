# -*- coding: utf-8 -*-
h,w = map(int, input().split())
n = int(input())

l = []
a = [int(x) for x in input().split()]
for i in range(n):
    l.extend([i+1 for _ in range(a[i])])

for hi in range(h):
    line = []
    for wi in range(w):
        line.append(l[w*hi+wi])
    if hi%2==1:
        line = line[::-1]

    print(*line)

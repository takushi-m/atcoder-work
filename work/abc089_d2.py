# -*- coding: utf-8 -*-
h,w,d = map(int, input().split())
dd = {}
field = []
for hi in range(h):
    line = list(map(int, input().split()))
    field.append(line)
    for wi in range(w):
        dd[line[wi]] = (hi, wi)
q = int(input())
lr = [list(map(int, input().split())) for _ in range(q)]

memo = [[-1 for _ in range(h*w)] for _ in range(h*w)]
for i in range(1,d+1):
    s = i
    r = (i+d*(10**5))%(h*w+1)
    res = 0
    while s!=r:
        h1,w1 = dd[s]
        s2 = field[h1][w1]
        h2,w2 = dd[s2]
        res += abs(h1-h2) + abs(w1-w2)
        memo[i][w2] = res

for (l,r) in lr:
    print(calc(l,r))

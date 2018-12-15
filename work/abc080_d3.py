# -*- coding: utf-8 -*-
from operator import itemgetter

N,C = map(int, input().split())
T = 0
record = []
for _ in range(N):
    s,t,c = map(int, input().split())
    T = max(T, t)
    record.append((s,t,c))
record.sort(key=itemgetter(2,0,1))

tl = [0]*(T+1)
curr_channel = None
for r in record:
    s,t,c = r
    if curr_channel==c:
        if curr_time==s:
            tl[s] += 1
            tl[t] -= 1
        else:
            tl[s-1] += 1
            tl[t] -= 1
        curr_time = t
    else:
        tl[s-1] += 1
        tl[t] -= 1
        curr_channel = c
        curr_time = t

s = 0
res = 0
for t in tl:
    s += t
    res = max(res, s)
print(res)

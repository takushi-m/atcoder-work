# -*- coding: utf-8 -*-
n,c = map(int, input().split())
tv = []
T = 0
for _ in range(n):
    line = list(map(int, input().split()))
    T = max(T, line[1])
    tv.append(line)

rm = [0 for _ in range(2*T)]

for ci in range(c):
    tt = [0 for _ in range(2*T)]
    for i in range(n):
        if tv[i][2]==ci+1:
            tt[2*tv[i][0]-2] += 1
            tt[2*tv[i][1]-1] -= 1
    for t in range(2*T-1):
        tt[t+1] = tt[t+1]+tt[t]
    for t in range(2*T):
        if tt[t]>0:
            rm[t] += 1
    # print(tt)
# print(rm)
ret = 0
for s in rm:
    ret = max(ret, s)
print(ret)

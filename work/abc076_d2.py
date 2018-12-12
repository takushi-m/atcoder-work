# -*- coding: utf-8 -*-
n = int(input())
tl = list(map(int, input().split()))
vl = list(map(int, input().split()))
T = sum(tl)

conditions = []
t = 0
conditions.append((t,t,0))
for i in range(n):
    conditions.append((t,t+tl[i],vl[i]))
    t += tl[i]
conditions.append((t,t,0))

def calc_v(t):
    maxv = 1000
    for (lt,rt,v) in conditions:
        if t<=lt:
            maxv = min(maxv, v+(lt-t))
        elif lt<t<rt:
            maxv = min(maxv, v)
        else:
            maxv = min(maxv, v+(t-rt))
    return maxv

res = 0
for i in range(2*T):
    t = i*0.5
    res += (calc_v(t)+calc_v(t+0.5))*0.5/2.0

print(res)

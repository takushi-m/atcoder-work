# -*- coding: utf-8 -*-
n = int(input())
d = {}

for x in input().split():
    a = int(x)
    if a not in d:
        d[a] = 0
    d[a] += 1

ret1 = 0
ret2 = 0
kk = list(d.keys())
kk.sort(reverse=True)
for k in kk:
    if d[k]>=4 and ret1==0:
        ret1 = k**2
        if ret2==0:
            break
    if d[k]>=2:
        if ret2==0:
            ret2 = k
        elif ret2>0:
            ret2 *= k
            break
print(max(ret1,ret2))

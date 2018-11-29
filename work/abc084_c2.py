# -*- coding: utf-8 -*-
n = int(input())
csf = []
for _ in range(n-1):
    c,s,f = map(int, input().split())
    csf.append((c,s,f))

for i in range(n-1):
    t = 0
    for j in range(i,n-1):
        t = max(t, csf[j][1])
        if t%csf[j][2]>0:
            t += (csf[j][2] - t%csf[j][2])
        t += csf[j][0]
    print(t)
print(0)

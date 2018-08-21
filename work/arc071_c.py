# -*- coding: utf-8 -*-
n = int(input())

a = "abcdefghijklmnopqrstuvwxyz"
d = {}
for c in a:
    d[c] = 0

for i in range(n):
    dd = {}
    for c in list(input()):
        if c not in dd:
            dd[c] = 0
        dd[c] += 1

    if i==0:
        for c in dd.keys():
            d[c] = dd[c]
    else:
        for c in a:
            if c in dd and d[c]>0 and dd[c]<d[c]:
                d[c] = dd[c]
            elif d[c]>0 and c not in dd:
                d[c] = 0

ret = ""
for c in a:
    if d[c]!=100:
        ret += c*d[c]
print(ret)

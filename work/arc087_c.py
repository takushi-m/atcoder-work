# -*- coding: utf-8 -*-
n = int(input())

d = {}
ret = 0
for x in input().split():
    a = int(x)
    if a not in d:
        d[a] = 0

    if d[a] == a:
        ret += 1
    else:
        d[a] += 1

for k,v in d.items():
    if k!=v:
        ret += v
print(ret)

# -*- coding: utf-8 -*-

n = int(input())

s = 0
d = {}
for x in [int(a) for a in input().split(" ")]:
    s = s + x
    if s not in d:
        d[s] = 0
    d[s] = d[s]+1

ret = 0
for x in d:
    if d[x]>1:
        ret = ret + d[x]*(d[x]-1)//2
    if x==0:
        ret = ret + d[x]

print(ret)

# -*- coding: utf-8 -*-
n = int(input())
d = {}

for x in input().split():
    x = int(x)
    if x not in d:
        d[x] = 0
    d[x] += 1

cnt = 0
dcnt = 0
for k in d.keys():
    if d[k]%2==1:
        cnt += 1
    else:
        dcnt += 1

if dcnt%2==0:
    print(cnt+dcnt)
else:
    print(cnt+dcnt-1)

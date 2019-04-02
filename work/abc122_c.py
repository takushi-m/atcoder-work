# -*- coding: utf-8 -*-
n,q = map(int, input().split())
s = input()
lr = [list(map(int, input().split())) for _ in range(q)]

acc = []
for i in range(n+1):
    if i==0:
        acc.append(0)
    else:
        if s[i-2:i]=="AC":
            acc.append(acc[-1]+1)
        else:
            acc.append(acc[-1])
for l,r in lr:
    print(acc[r]-acc[l])

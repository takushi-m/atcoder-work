# -*- coding: utf-8 -*-
n,k,q = map(int, input().split())
p = [0]*n

for _ in range(q):
    ai = int(input())-1
    p[ai] += 1

for a in p:
    if k-(q-a)>0:
        print("Yes")
    else:
        print("No")

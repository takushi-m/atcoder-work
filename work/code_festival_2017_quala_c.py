# -*- coding: utf-8 -*-
from collections import Counter
h,w = map(int, input().split())
al = []
for _ in range(h):
    al += list(input())

c = Counter(al)

if h%2==1 and w%2==1:
    for k in c.keys():
        if c[k]%2==1:
            c[k] -= 1
            break

g4 = (h//2)*(w//2)*4
for k in c.keys():
    while c[k]>=4 and g4>0:
        c[k] -= 4
        g4 -= 4
if g4>0:
    print("No")
    exit()

g2 = (h%2)*(w//2)*2 + (w%2)*(h//2)*2
for k in c.keys():
    while c[k]>=2 and g2>0:
        c[k] -= 2
        g2 -= 2
if g2>0:
    print("No")
    exit()

for k in c.keys():
    if c[k]>0:
        print("No")
        exit()
print("Yes")

# -*- coding: utf-8 -*-
from itertools import permutations

n = int(input())
p = "".join(input().split())
q = "".join(input().split())

l = []
for s in permutations(range(1,n+1)):
    l.append("".join(map(str,s)))

l = sorted(l)

a = 0
b = 0
for i in range(len(l)):
    if l[i]==p:
        a = i+1
    if l[i]==q:
        b = i+1

print(abs(a-b))
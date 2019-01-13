# -*- coding: utf-8 -*-
n = int(input())
a,b = map(int, input().split())
pl = list(map(int, input().split()))

na = 0
nb = 0
nc = 0
for p in pl:
    if p<=a:
        na += 1
    elif a+1<=p<=b:
        nb += 1
    else:
        nc += 1

print(min(na,nb,nc))

# -*- coding: utf-8 -*-
from collections import Counter

n = int(input())
al = list(map(int, input().split()))

if max(al)==0:
    print("Yes")
    exit()

d = Counter(al)
keys = sorted(d.keys())
if len(keys)==2:
    if n%3==0 and keys[0]==0 and d[keys[0]]*2==d[keys[1]]:
        print("Yes")
        exit()

if len(keys)==3:
    if n%3==0 and keys[0]^keys[1]^keys[2]==0 and d[keys[0]]==d[keys[1]]==d[keys[2]]:
        print("Yes")
        exit()

print("No")
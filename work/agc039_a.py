# -*- coding: utf-8 -*-
from collections import Counter

def count(s):
    cnt = 1
    res = 0
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            cnt += 1
        else:
            res += cnt//2
            cnt = 1
    res += cnt//2
    return res

s = input()
k = int(input())

c = Counter(s)

if len(c.keys())==1:
    print(len(s)*k//2)
    exit()

if s[0]!=s[-1]:
    print(count(s)*k)
    exit()

cs = count(s)
cs2 = count(s+s)
print((cs2-cs)*(k-1) + cs)
# -*- coding: utf-8 -*-
from string import ascii_lowercase

s = list(input())
n = len(s)
k = int(input())

d = {}
d2 = {}
for i in range(len(ascii_lowercase)):
    c = ascii_lowercase[i]
    d[c] = (len(ascii_lowercase)-i)%len(ascii_lowercase)
    d2[c] = i

for i in range(n):
    if s[i]!="a" and d[s[i]]<=k:
        k -= d[s[i]]
        s[i] = "a"

if k>0:
    k %= len(ascii_lowercase)
    s[-1] = ascii_lowercase[(d2[s[-1]]+k)%len(ascii_lowercase)]

print("".join(s))

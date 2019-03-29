# -*- coding: utf-8 -*-
n = int(input())
s = {}
for _ in range(n):
    c = input()
    if c not in s:
        s[c] = 0
    s[c] += 1

m = int(input())
t = {}
for _ in range(m):
    c = input()
    if c not in t:
        t[c] = 0
    t[c] += 1

res = 0
for k in s.keys():
    r = s[k]
    if k in t:
        r -= t[k]
    res = max(res, r)

for k in t.keys():
    r = 0
    if k in s:
        r += s[k]
    r -= t[k]
    res = max(res, r)

print(res)

# -*- coding: utf-8 -*-
s = list(input())
n = len(s)

res = 10**5
for i in range(n-2):
    x = int("".join(s[i:i+3]))
    res = min(res, abs(753-x))
print(res)

# -*- coding: utf-8 -*-
s = input()
t = input()
n = len(s)

ds = {}
dt = {}
for i in range(n):
    if s[i] not in ds:
        ds[s[i]] = t[i]
    elif ds[s[i]]!=t[i]:
        print("No")
        exit()
    if t[i] not in dt:
        dt[t[i]] = s[i]
    elif dt[t[i]]!=s[i]:
        print("No")
        exit()
print("Yes")

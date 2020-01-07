# -*- coding: utf-8 -*-
s = input()
n = len(s)

cnt = 0
for i in range(n//2):
    j = n-1-i
    if i==j:
        continue

    if s[i]!=s[j]:
        cnt += 1

print(cnt)
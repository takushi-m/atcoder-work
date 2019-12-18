# -*- coding: utf-8 -*-
n = int(input())
s = input()

cnt = 0
i = 0
while i<n:
    j = i
    while j<n and s[i]==s[j]:
        j += 1
    i = j
    cnt += 1

print(cnt)
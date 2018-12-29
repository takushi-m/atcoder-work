# -*- coding: utf-8 -*-
s = list(input())
n = len(s)

l = []
for i in range(n):
    if s[i]=="B":
        l.append(i)

l.sort(reverse=True)

res = 0
cnt = 0
for idx in l:
    res += n-idx-1 - cnt
    cnt += 1

print(res)

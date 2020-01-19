# -*- coding: utf-8 -*-
n = int(input())
pl = list(map(int, input().split()))

m = []
mm = 10**8
for i in range(n):
    mm = min(mm,pl[i])
    m.append(mm)

res = 0
for i in range(n):
    if pl[i]==m[i]:
        res += 1

print(res)
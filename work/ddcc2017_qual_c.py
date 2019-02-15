# -*- coding: utf-8 -*-
n,c = map(int, input().split())
l = [int(input()) for _ in range(n)]
l.sort()

res = 0
m = n-1
i = 0
while i<m:
    if l[i]+l[m]+1<=c:
        res += 1
        i += 1
        m -= 1
        continue
    else:
        res += 1
        m -= 1
if i==m:
    res += 1
print(res)

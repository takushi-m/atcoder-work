# -*- coding: utf-8 -*-
a,b = map(int, input().split())

res = 0
cnt = 1
while cnt<b:
    cnt += a-1
    res += 1
print(res)

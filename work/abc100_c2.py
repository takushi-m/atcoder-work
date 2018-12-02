# -*- coding: utf-8 -*-
n = int(input())
al = list(map(int, input().split()))
res = 0
for a in al:
    t = 0
    while a%2==0:
        a //= 2
        t += 1
    res += t
print(res)

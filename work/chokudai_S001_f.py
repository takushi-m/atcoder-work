# -*- coding: utf-8 -*-
n = int(input())
al = list(map(int, input().split()))

c = 0
m = 0
for a in al:
    if m<a:
        c += 1
        m = a

print(c)
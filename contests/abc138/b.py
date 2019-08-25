# -*- coding: utf-8 -*-
n = int(input())
al = list(map(int, input().split()))

r = 0
for a in al:
    r += 1/a

print(1/r)

# -*- coding: utf-8 -*-
n = int(input())
cnt = 0
s = 0
for _ in range(n):
    x = int(input())
    if x==0:
        cnt += s//2
        s = 0
    else:
        s += x
print(cnt+s//2)

# -*- coding: utf-8 -*-
h = int(input())

cnt = 0
b = 1
while h>1:
    h //= 2
    cnt += b
    b *= 2
print(cnt+b)

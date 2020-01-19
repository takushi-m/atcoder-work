# -*- coding: utf-8 -*-
x,y = map(int, input().split())
cnt = 0
b = 1
while x*b<=y:
    cnt += 1
    b *= 2

print(cnt)
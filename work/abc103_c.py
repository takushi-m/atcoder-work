# -*- coding: utf-8 -*-
n = input()
ret = 0
for a in input().split(" "):
    a = int(a)
    ret += a-1

print(ret)

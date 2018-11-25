# -*- coding: utf-8 -*-
s = input()
w = int(input())

ret = ""
for i in range(0,len(s),w):
    ret += s[i]

print(ret)

# -*- coding: utf-8 -*-
s = input()

res = ""
for c in s:
    if c=="B" and len(res)>0:
        res = res[:-1]
    elif c!="B":
        res += c

print(res)
# -*- coding: utf-8 -*-
s = list(input())
n = len(s)

ret = 0
up = 0
down = 0
for i in range(n):
    if s[i]=="D":
        # print(i,up,down)
        ret += i + up + 2*down
    else:
        # print(i,up,down)
        ret += 2*i + up + 2*down

    if s[i]=="U":
        up += 1
    else:
        down += 1
print(ret)

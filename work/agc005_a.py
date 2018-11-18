# -*- coding: utf-8 -*-
x = input()
n = len(x)
r = 0
cnt = 0
for i in range(n):
    if x[i]=="S":
        cnt += 1
    else:
        if cnt>0:
            r += 2
            cnt -= 1

print(n-r)

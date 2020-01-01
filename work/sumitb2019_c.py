# -*- coding: utf-8 -*-
x = int(input())

l = [0]*(x+1)
l[0] = 1
for i in range(1,x+1):
    for j in range(100,106):
        if i-j>=0:
            l[i] += l[i-j]

if l[x]>0:
    print(1)
else:
    print(0)
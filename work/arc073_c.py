# -*- coding: utf-8 -*-

line =  input().split()
n = int(line[0])
T = int(line[1])
t = [int(x) for x in input().split()]

ret = T
for i in range(n-1):
    if t[i+1]-t[i]>=T:
        ret += T
    else:
        ret += t[i+1]-t[i]
print(ret)

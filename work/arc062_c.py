# -*- coding: utf-8 -*-
import math
n = int(input())
T = 1
A = 1
for _ in range(n):
    line = input().split(" ")
    t = int(line[0])
    a = int(line[1])
    c = max((T+t-1)//t, (A+a-1)//a)
    T = c*t
    A = c*a

print(A+T)

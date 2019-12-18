# -*- coding: utf-8 -*-
from math import sqrt,floor
n = int(input())

x = floor(sqrt(n))
for i in range(x,-1,-1):
    if n%i==0:
        print(i+n//i-2)
        exit()

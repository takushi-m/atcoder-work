# -*- coding: utf-8 -*-
line = input().split()
n = int(line[0])
m = int(line[1])

if n >= m//2:
    print(m//2)
else:
    print(n + (m-2*n)//4)

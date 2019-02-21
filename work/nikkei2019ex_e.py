# -*- coding: utf-8 -*-
p = int(input())

if p==0:
    print(1)
    exit()

x = 1789997546303
for _ in range(1000-p):
    if x%2==0:
        x //= 2
    else:
        x = 3*x+1
print(x)

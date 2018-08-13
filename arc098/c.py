# -*- coding: utf-8 -*-
line = input().split(" ")
n = int(line[0])
k = int(line[1])
q = int(line[2])
a = sorted([int(x) for x in input().split(" ")])

print(a[q-1]-a[0])

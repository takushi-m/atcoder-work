# -*- coding: utf-8 -*-
line = input().split(" ")
n = int(line[0])
k = int(line[1])

l = []
for _ in range(n):
    line = input().split(" ")
    a = int(line[0])
    b = int(line[1])
    l.append([a,b])

l.sort()

while k>0:
    x = l.pop(0)
    k = k-x[1]

print(x[0])

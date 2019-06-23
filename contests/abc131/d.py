# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline
n = int(input())
ab = []
for _ in range(n):
    a,b = map(int, input().split())
    ab.append((a,b))

ab.sort(key=lambda x:x[1])

t = 0
for i in range(n):
    t += ab[i][0]
    if t>ab[i][1]:
        print("No")
        exit()
print("Yes")

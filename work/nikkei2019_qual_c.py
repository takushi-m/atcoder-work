# -*- coding: utf-8 -*-
n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]

ab.sort(reverse=True, key=lambda c:c[0]+c[1])

t = 0
a = 0
for i in range(n):
    if i%2==0:
        t += ab[i][0]
    else:
        a += ab[i][1]

print(t-a)

# coding=utf-8

n = 5

for i in range(1<<n):
    s = []
    for j in range(n):
        if i & (1<<j):
            s.append(j)
    print(s)

from itertools import combinations

for i in range(n+1):
    for t in combinations(range(n), i):
        print(t)

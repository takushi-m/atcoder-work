# coding=utf-8
from itertools import combinations

line = input().split(" ")
line = list(map(lambda x:int(x), line))

r = []
for t in combinations(line, 3):
    r.append(sum(t))

r = list(set(r))
r.sort(reverse=True)

print(r[2])

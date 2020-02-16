# -*- coding: utf-8 -*-
from collections import defaultdict
n = int(input())
d = defaultdict(int)

for _ in range(n):
    s = input()
    d[s] += 1

l = []
for k in d:
    l.append((d[k],k))
l.sort(key=lambda x:(-x[0],x[1]))
m = l[0][0]
i = 0
while i<len(l) and l[i][0]==m:
    print(l[i][1])
    i += 1
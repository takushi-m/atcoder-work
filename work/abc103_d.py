# -*- coding: utf-8 -*-
from operator import itemgetter

n,m = map(int, input().split())
ab = []
for _ in range(m):
    line = list(map(int, input().split()))
    ab.append(line)

ab = sorted(ab, key=itemgetter(1))

cnt = 1
bridge = ab[0][1]-1
for i in range(1,m):
    if ab[i][0]<=bridge and bridge<ab[i][1]:
        continue
    else:
        cnt += 1
        bridge = ab[i][1]-1
print(cnt)

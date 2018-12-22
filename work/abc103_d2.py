# -*- coding: utf-8 -*-
from operator import itemgetter

n,m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]
ab.sort(key=itemgetter(1,0))

cnt = 0
cb = -1
for (a,b) in ab:
    if cb == -1:
        cb = b - 1
        cnt += 1
    elif a<=cb:
        continue
    else:
        cb = b - 1
        cnt += 1

print(cnt)

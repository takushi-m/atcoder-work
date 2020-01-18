# -*- coding: utf-8 -*-
from operator import itemgetter
n = int(input())
xl = [list(map(int, input().split())) for _ in range(n)]
lr = sorted([[xl[i][0]-xl[i][1],xl[i][0]+xl[i][1]] for i in range(n)], key=itemgetter(1,0))

cnt = 1
cl = lr[0][0]
cr = lr[0][1]
for l,r in lr[1:]:
    if cr<=l:
        cr = r
        cl = l
        cnt += 1

print(cnt)
# -*- coding: utf-8 -*-
from itertools import permutations

N,C = map(int, input().split())
D = []
for _ in range(C):
    line = list(map(int, input().split()))
    D.append(line)
c = []
t = [[0 for _ in range(C)] for _ in range(3)]
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        r = (i+j)%3
        t[r][line[j]-1] += 1
    c.append(line)

def e(conv):
    ret = 0
    for r in range(3):
        for i in range(C):
            ret += t[r][i]*D[i][conv[r]-1]

    return ret

ret = 10**10
for conv in permutations(range(1,C+1), 3):
    ret = min(ret, e(conv))

print(ret)

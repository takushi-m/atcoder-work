# -*- coding: utf-8 -*-
from math import sqrt
from random import randint, shuffle
import time
from pprint import pprint
start = time.time()
n = int(input())
xy = []

def dis(i,j):
    return (xy[i][0]-xy[j][0])**2 + (xy[i][1]-xy[j][1])**2

def score(path):
    d = []
    for i in range(n-1):
        d.append(dis(i,i+1))
    d.append(dis(n-1,0))
    avg = sum(d)/n
    return sum([(d[i]-avg)**2 for i in range(n)])

diff = 0
table = [[[] for _ in range(4)] for _ in range(4)]
for i in range(n):
    x,y = map(int, input().split())
    xy.append((x,y))
    xi = x//126
    yi = y//126
    table[xi][yi].append(i)
    for d in [[diff,0],[0,diff],[-diff,0],[0,-diff]]:
        xi = (x+d[0])//126
        yi = (y+d[1])//126
        if 4>xi>=0 and 4>yi>=0:
            table[xi][yi].append(i)

used = [False for _ in range(n)]
def pick(xi,yi,i):
    if i<len(table[xi][yi]) and not used[table[xi][yi][i]]:
        used[table[xi][yi][i]] = True
        return table[xi][yi][i]

res = []
for i in range(n):
    res.append(pick(1,1,i))
    res.append(pick(0,1,i))
    res.append(pick(0,0,i))
    res.append(pick(1,0,i))
    res.append(pick(2,0,i))
    res.append(pick(3,0,i))
    res.append(pick(3,1,i))
    res.append(pick(3,2,i))
    res.append(pick(3,3,i))
    res.append(pick(2,3,i))
    res.append(pick(1,3,i))
    res.append(pick(0,3,i))
    res.append(pick(0,2,i))
    res.append(pick(1,2,i))
    res.append(pick(2,2,i))
    res.append(pick(2,1,i))

tmp = []
for p in res:
    if p is not None:
        tmp.append(p)
res = tmp


tmp = []
for i in range(n):
    if i==n-1:
        tmp.append((i, dis(res[n-1],res[0])))
    else:
        tmp.append((i, dis(res[i],res[i+1])))
tmp.sort()

mini = tmp[0][0]
maxi = tmp[-1][0]
res[mini],res[maxi] = res[maxi],res[mini]

for p in res:
    print(p)

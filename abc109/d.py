# -*- coding: utf-8 -*-
from pprint import pprint
h,w = map(int, input().split())
m = []
for _ in range(h):
    line = [int(x) for x in input().split()]
    m.append(line)

ret = []
for i in range(h):
    j = 0
    while j<w:
        if m[i][j]%2==1:
            jj = j+1
            while jj<w and m[i][jj]%2==0:
                jj += 1
            if jj==w:
                jj = w-1
            for dj in range(j,jj):
                ret.append([i,dj,i,dj+1])
            if m[i][jj]%2==1:
                m[i][j] -= 1
                m[i][jj] += 1
            elif jj == w-1:
                m[i][j] -= 1
                m[i][jj] += 1
        j += 1

i = 0
while i<h:
    if m[i][w-1]%2==1:
        ii = i+1
        while ii<h and m[ii][w-1]%2==0:
            ii += 1
        if ii==h:
            ii = h-1
        for di in range(i,ii):
            ret.append([di,w-1,di+1,w-1])
        if m[ii][w-1]%2==1:
            m[i][w-1] -= 1
            m[ii][w-1] += 1
    i += 1

print(len(ret))
for r in ret:
    print(r[0]+1,r[1]+1,r[2]+1,r[3]+1)

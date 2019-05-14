# -*- coding: utf-8 -*-
from math import ceil

def max_flow(edge):
    """
    edgeは隣接リスト。リストは辺の行き先と容量のタプル
    """
    





r,c = map(int, input().split())
cl = [list(input()) for _ in range(r)]

group = [[0]*c for _ in range(r)]
g = 0
for ri in range(r):
    for ci in range(c):
        if cl[ri][ci]=="." and group[ri][ci]==0:
            g += 1
            q = [(ri,ci)]
            group[ri][ci] = g
            while len(q)>0:
                rj,cj = q.pop(0)
                for d in [[1,0],[0,1],[-1,0],[0,-1]]:
                    if r>rj+d[0]>=0 and c>cj+d[1]>=0:
                        if cl[rj+d[0]][cj+d[1]]=="." and group[rj+d[0]][cj+d[1]]==0:
                            group[rj+d[0]][cj+d[1]] = g
                            q.append((rj+d[0],cj+d[1]))

res = 0

used = set()
for ri in range(r):
    for ci in range(c):
        if cl[ri][ci]=="." and group[ri][ci]>0 and group[ri][ci] not in used:
            g = group[ri][ci]
            used.add(g)

            q = [(ri,ci,0)]
            selected = set()
            cnt1 = 0
            while len(q)>0:
                rj,cj,f = q.pop(0)
                for d in [[1,0],[0,1],[-1,0],[0,-1]]:
                    if r>rj+d[0]>=0 and c>cj+d[1]>=0:
                        if group[rj+d[0]][cj+d[1]]==g and (rj+d[0],cj+d[1]) not in selected:
                            selected.add((rj+d[0],cj+d[1]))
                            if (f+1)%2==0:
                                cnt1 += 1
                            q.append((rj+d[0],cj+d[1],f+1))

            q = [(ri,ci,1)]
            selected = set()
            cnt2 = 1
            while len(q)>0:
                rj,cj,f = q.pop(0)
                for d in [[1,0],[0,1],[-1,0],[0,-1]]:
                    if r>rj+d[0]>=0 and c>cj+d[1]>=0:
                        if group[rj+d[0]][cj+d[1]]==g and (rj+d[0],cj+d[1]) not in selected:
                            selected.add((rj+d[0],cj+d[1]))
                            if (f+1)%2==0:
                                cnt2 += 1
                            q.append((rj+d[0],cj+d[1],f+1))

            res += max(cnt1,cnt2)
print(res)

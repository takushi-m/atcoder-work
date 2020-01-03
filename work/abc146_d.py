# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10**5+10)

n = int(input())
visited = set()
g = {}
idx = {}
color = {}
for i in range(n-1):
    a,b = map(int, input().split())
    idx[i] = (a,b)
    if a not in g:
        g[a] = []
    g[a].append(b)
    if b not in g:
        g[b] = []
    g[b].append(a)

def dfs(v,c):
    cc = 0
    for u in g[v]:
        if u in visited:
            continue
        visited.add(u)

        cc += 1
        while cc==c:
            cc += 1
        a,b = min(u,v),max(u,v)
        color[(a,b)] = cc
        
        dfs(u,cc)
visited.add(1)
dfs(1,0)

mc = 0
for c in color.values():
    mc = max(mc, c)
print(mc)
for i in range(n-1):
    print(color[idx[i]])
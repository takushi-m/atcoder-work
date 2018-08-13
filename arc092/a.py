# coding=utf-8
from pprint import pprint
n = int(input())
red = []
blue = []

for _ in range(n):
    line = input().split(" ")
    red.append((int(line[0]), int(line[1])))

for _ in range(n):
    line = input().split(" ")
    blue.append((int(line[0]), int(line[1])))

g = []
for _ in range(2*n):
    g.append([])
match = [-1 for _ in range(2*n)]
used = [False for _ in range(2*n)]

def add_edge(v, u):
    g[u].append(v)
    g[v].append(u)

for (ri,r) in enumerate(red):
    for (bi,b) in enumerate(blue):
        if r[0]<b[0] and r[1]<b[1]:
            add_edge(ri, n+bi)

def dfs(v):
    used[v] = True
    for u in g[v]:
        w = match[u]
        if w<0 or not used[w] and dfs(w):
            match[v] = u
            match[u] = v
            return True
    return False

cnt = 0
for v in range(n):
    if match[v]<0:
        used = [False for _ in range(2*n)]
        if dfs(v):
            cnt += 1
print(cnt)

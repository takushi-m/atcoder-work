# coding=utf-8

INF = 10**9 + 1
n = int(input())
V = []

for _ in range(n):
    line = input().split(" ")
    V.append((int(line[0]), int(line[1])))

def cost(vi, ui):
    v = V[vi]
    u = V[ui]
    return min(abs(v[0]-u[0]), abs(v[1]-u[1]))

mincost = [INF for _ in range(n)]
used = [False for _ in range(n)]

mincost[0] = 0
ret = 0

while True:
    v = -1
    for u in range(n):
        if not used[u] and (v==-1 or mincost[u]<mincost[v]):
            v = u
    if v==-1:
        break

    used[v] = True
    ret += mincost[v]

    for u in range(n):
        mincost[u] = min(mincost[u], cost(v,u))

print(ret)

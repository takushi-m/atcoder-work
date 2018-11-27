# -*- coding: utf-8 -*-
n,m = map(int, input().split())
edge = [[] for _ in range(n)]
ab = []
for _ in range(m):
    a,b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)
    ab.append((a,b))

def check(a,b):
    visited = [False for _ in range(n)]
    stack = [0]
    while len(stack)>0:
        e = stack.pop()
        visited[e] = True
        for v in edge[e]:
            if (e==a and v==b) or (e==b and v==a):
                continue
            if not visited[v]:
                stack.append(v)
    return all(visited)

res = 0
for a,b in ab:
    if not check(a,b):
        res += 1
print(res)

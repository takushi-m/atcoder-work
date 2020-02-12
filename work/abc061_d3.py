# -*- coding: utf-8 -*-
def bellmanFord(e,n,s):
    inf = 10**18
    d = [inf]*n
    d[s] = 0

    loop = False
    for i in range(n):
        updated = False
        for v in range(n):
            for u,c in e[v]:
                if d[v]!=inf and d[u]>d[v]+c:
                    d[u] = d[v]+c
                    updated = True
                    if i==n-1 and u==n-1:
                        loop = True
        if not updated:
            break
    return d,loop


n,m = map(int, input().split())
e = [[] for _ in range(n)]
for _ in range(m):
    a,b,c = map(int, input().split())
    a -= 1
    b -= 1
    e[a].append((b,-c))

d,loop = bellmanFord(e,n,0)
if loop:
    print("inf")
else:
    print(-d[n-1])
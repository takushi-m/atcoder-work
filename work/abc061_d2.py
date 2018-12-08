# -*- coding: utf-8 -*-
inf = 10**15
n,m = map(int, input().split())
edge = []
for _ in range(m):
    a,b,c = map(int, input().split())
    a -= 1
    b -= 1
    edge.append((a,b,c))

d = [inf for _ in range(n)]
d[0] = 0
for _ in range(n):
    update = False
    for i in range(m):
        a,b,c = edge[i]
        if d[a]<inf:
            if d[b]<inf:
                if d[b]<d[a]+c:
                    d[b] = d[a]+c
                    update = True
            else:
                update = True
                d[b] = d[a] + c
    if not update:
        break

ans = d[n-1]
updated = [False for _ in range(n)]
for _ in range(n):
    update = False
    for i in range(m):
        a,b,c = edge[i]
        if d[a]<inf:
            if d[a]+c>d[b]:
                d[b] = d[a] + c
                if not updated[b]:
                    update = True
                    updated[b] = True
        if updated[a] and not updated[b]:
            update = True
            updated[b] = True
    if not update:
        break

if updated[n-1]:
    print("inf")
else:
    print(ans)

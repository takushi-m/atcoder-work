# -*- coding: utf-8 -*-
n,m,k = map(int, input().split())
pl = list(map(int, input().split()))
edge = {}
for i in range(n):
    pl[i] -= 1
    p = pl[i]
    if p==-1:
        root = i
        continue
    if p not in edge:
        edge[p] = []
    edge[p].append(i)

used = [False]*n

def check(coin, node):
    q = [(root, 1)]
    hl = []
    node_h = -1
    while len(q)>0:
        u,h = q.pop(0)
        if u==node:
            node_h = h
            continue
        if used[u]:
            continue
        hl.append(h)
        if u in edge:
            for v in edge[u]:
                q.append((v,h+1))
    cnt = len(hl)
    r = m-coin-1
    if r>cnt:
        return False,node_h
    hmin = sum(hl[:r])
    hmax = sum(hl[-r:])
    if r==0:
        hmax = 0
    return hmin<=k-node_h<=hmax, node_h

res = []
for i in range(m):
    for j in range(n):
        if used[j]:
            continue
        f,h = check(i,j)
        if f:
            res.append(j)
            used[j] = True
            if j in edge:
                q = [j]
                while len(q):
                    u = q.pop(0)
                    used[u] = True
                    if u in edge:
                        for v in edge[u]:
                            q.append(v)
            k -= h
            break
if k==0 and len(res)==m:
    print(*[x+1 for x in res])
else:
    print(-1)

# -*- coding: utf-8 -*-
n = int(input())
e = [set() for _ in range(n)]
for i in range(n):
    a = int(input())-1
    e[i].add(a)
    e[a].add(i)

def dfs():
    col = [-1]*n
    for s in range(n):
        if col[s]>=0:
            continue
        col[s] = 0
        q = [s]
        while len(q)>0:
            v = q.pop()
            c = col[v]
            for u in e[v]:
                if col[u]<0:
                    col[u] = (c+1)%2
                    q.append(u)
                else:
                    if c==col[u]:
                        return False
    return True

if not dfs():
    print(-1)
    exit()

res = 0
col = [-1]*n
for s in range(n):
    if col[s]>=0:
        continue
    col[s] = 0
    num = [0,0]
    num[0] = 1
    q = [s]
    while len(q)>0:
        v = q.pop()
        for u in e[v]:
            if col[u]<0:
                col[u] = (col[v]+1)%2
                num[col[u]] += 1
                q.append(u)
    res += max(*num)

print(res)
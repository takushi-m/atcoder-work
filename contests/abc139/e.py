# -*- coding: utf-8 -*-
n = int(input())
al = [[] for _ in range(n+1)]
for i in range(n):
    a = list(map(int, input().split()))
    al[i+1] = [-1]+a
idx = [1 for _ in range(n+1)]
idx[0] = n
res = 0
while True:
    res += 1
    s = set()
    for i in range(1,n+1):
        used = [False for _ in range(n+1)]
        used[i] = True
        t = i
        if idx[t]>=n:
            continue
        u = al[t][idx[t]]
        if idx[u]>=n:
            continue
        v = al[u][idx[u]]
        while t!=v:
            t = u
            if used[t]:
                print(-1)
                exit()
            used[t] = True
            if idx[t]>=n:
                break
            u = al[t][idx[t]]
            if idx[u]>=n:
                break
            v = al[u][idx[u]]
        s.add(t)
        s.add(u)
    for i in s:
        idx[i] += 1
    flag = True
    for i in idx:
        if i<n:
            flag = False
            break
    if flag:
        break
print(res)

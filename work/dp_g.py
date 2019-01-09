# -*- coding: utf-8 -*-
n,m = map(int, input().split())
edge = [set() for _ in [0]*n]
for _ in range(m):
    x,y = map(int, input().split())
    x -= 1
    y -= 1
    edge[x].add(y)

res = 0
d = [-1]*n

for i in range(n):
    if d[i]>-1:
        continue
    st = [i]
    d[i] = 0
    while len(st)>0:
        s = st.pop()
        for v in edge[s]:
            d[v] = max(d[v], d[s]+1)
            st.append(v)

print(max(d))

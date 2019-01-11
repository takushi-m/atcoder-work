# -*- coding: utf-8 -*-
from collections import deque

n,m = map(int, input().split())
edge = [set() for _ in [0]*n]
iny = [0 for _ in [0]*n]
for _ in range(m):
    x,y = map(int, input().split())
    x -= 1
    y -= 1
    edge[x].add(y)
    iny[y] += 1

# from random import randint
# n = 10**1
# m = 10**1
# edge = [set() for _ in [0]*n]
# for _ in range(m):
#     x = randint(0,n-1)
#     y = randint(0,n-1)
#     while x==y:
#         x = randint(0,n-1)
#         y = randint(0,n-1)
#
#     edge[x].add(y)

res = 0
d = [0]*n
for i in [j for j in range(n) if iny[j]==0]:
    if d[i]>0:
        continue
    st = deque([i])
    while len(st)>0:
        s = st.popleft()
        for v in edge[s]:
            if d[v]<d[s]+1:
                d[v] = d[s]+1
                st.append(v)

print(max(d))

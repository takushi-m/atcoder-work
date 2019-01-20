# -*- coding: utf-8 -*-
from collections import deque
n,k = map(int, input().split())
td = []

for _ in range(n):
    t,d = map(int, input().split())
    td.append((t,d))

td.sort(reverse=True, key=lambda x:x[1])

used = set()
q = []
res = 0
kind = 0
for i in range(k):
    t,d = td[i]
    if t not in used:
        kind += 1
        used.add(t)
    else:
        q.append((t,d))
    res += d
res += kind**2
q = deque(sorted(q, key=lambda x:x[1]))

tmp = res
for i in range(k,n):
    if len(q)==0:
        break
    t2,d2 = td[i]
    if t2 in used:
        continue
    used.add(t2)
    t,d = q.popleft()

    r = tmp - d + d2
    r -= kind**2
    kind += 1
    r += kind**2
    res = max(res, r)
    tmp = r

print(res)

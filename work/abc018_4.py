from itertools import combinations
from collections import defaultdict

n,m,p,q,r = map(int, input().split())

d = {}
for i in range(n):
    d[i] = []
for _ in range(r):
    x,y,z = map(int, input().split())
    x -= 1
    y -= 1
    d[x].append((y,z))

res = -1
for c in combinations(range(n),p):
    dd = defaultdict(int)
    for i in c:
        for y,z in d[i]:
            dd[y] += z
    l = []
    for v in dd.values():
        l.append(v)
    l.sort(reverse=True)
    l = l[:q]
    res = max(res, sum(l))

print(res)
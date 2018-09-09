# -*- coding: utf-8 -*-
inf = 10**50
n,m = map(int, input().split())

ea = []
eb = []
cost = []

for _ in range(m):
    a,b,c = map(int, input().split())
    a -= 1
    b -= 1
    ea.append(a)
    eb.append(b)
    cost.append(-c)

d = [inf for _ in range(n)]
d[0] = 0
for _ in range(n):
    update = False
    for i in range(m):
        a = ea[i]
        b = eb[i]
        c = cost[i]
        if d[a]!=inf and d[b]>d[a]+c:
            d[b] = d[a]+c
            update = True
    if not update:
        break

ans = d[n-1]
negative = [False for _ in range(n)]
for _ in range(n):
    update = False
    for i in range(m):
        a = ea[i]
        b = eb[i]
        c = cost[i]
        if d[a]!=inf and d[b]>d[a]+c:
            d[b] = d[a]+c
            if not negative[b]:
                update = True
            negative[b] = True
        if negative[a] and not negative[b]:
            negative[b] = True
            update = True
    if not update:
        break
# print(d)
if negative[n-1]:
    print("inf")
else:
    print(-ans)

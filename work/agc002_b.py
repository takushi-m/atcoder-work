# -*- coding: utf-8 -*-
n,m = map(int, input().split())
s = set([1])
d = {}
d[1] = 1

for _ in range(m):
    x,y = map(int, input().split())
    if x not in d:
        d[x] = 0
    else:
        d[x] -= 1
    if y not in d:
        d[y] = 2
    else:
        d[y] += 1
    if x in s:
        if x in d and d[x]==0:
            s.remove(x)
        s.add(y)
# print(d)
# print(s)
print(len(s))

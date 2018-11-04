# -*- coding: utf-8 -*-

n,m = map(int, input().split())
d = {}
py = []
for i in range(1,m+1):
    p,y = map(int, input().split())
    py.append((p,y))
    if p not in d:
        d[p] = []
    d[p].append([y,i])

ret = {}
for k in d.keys():
    d[k] = sorted(d[k])
    ret[k] = {}
    for i in range(len(d[k])):
        ret[k][d[k][i][0]] = i+1

for p,y in py:
    print("{:06}{:06}".format(p,ret[p][y]))

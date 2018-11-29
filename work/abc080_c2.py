# -*- coding: utf-8 -*-
n = int(input())
f = []
for _ in range(n):
    f.append(input().split())
p = []
for _ in range(n):
    p.append(list(map(int, input().split())))

res = None
for i in range(1,2**10):
    joisino = [str(i>>n&1) for n in range(10)]
    prof = 0
    for j in range(n):
        c = 0
        for k in range(10):
            if joisino[k]=="1" and f[j][k]=="1":
                c += 1
        prof += p[j][c]
    if res is None:
        res = prof
    else:
        res = max(res, prof)
print(res)

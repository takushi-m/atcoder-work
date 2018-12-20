# -*- coding: utf-8 -*-
n,c = map(int, input().split())
d = [list(map(int, input().split())) for _ in range(c)]

cnt = {
    0: {},
    1: {},
    2: {}
}

for i in range(n):
    cl = list(map(int, input().split()))
    for j in range(n):
        k = (i+j)%3
        if cl[j] not in cnt[k]:
                cnt[k][cl[j]] = 0
        cnt[k][cl[j]] += 1

res = 10**3 * 500**2 + 10
for ci in range(c):
    for cj in range(c):
        if ci==cj:
            continue
        for ck in range(c):
            if ci==ck or cj==ck:
                continue

            t = 0
            cc = [ci, cj, ck]
            for r in range(3):
                for k in cnt[r].keys():
                    t += d[k-1][cc[r]]*cnt[r][k]
            res = min(res, t)
print(res)

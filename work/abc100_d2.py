# -*- coding: utf-8 -*-
n,m = map(int, input().split())
xyz = [list(map(int, input().split())) for _ in range(n)]

res = -1
for xi in [1,-1]:
    for yi in [1,-1]:
        for zi in [1,-1]:
            xyz.sort(reverse=True, key=lambda c:c[0]*xi+c[1]*yi+c[2]*zi)
            t = [0,0,0]
            for i in range(m):
                t[0] += xyz[i][0]
                t[1] += xyz[i][1]
                t[2] += xyz[i][2]

            res = max(res, abs(t[0])+abs(t[1])+abs(t[2]))

print(res)

# -*- coding: utf-8 -*-
n,m = map(int, input().split())
xyz = []
for _ in range(n):
    line = list(map(int, input().split()))
    xyz.append(line)

score = -1
for xo in [1,-1]:
    for yo in [1,-1]:
        for zo in [1,-1]:
            idx = sorted(range(n), reverse=True, key=lambda i:xo*xyz[i][0]+yo*xyz[i][1]+zo*xyz[i][2])
            X = 0
            Y = 0
            Z = 0
            for i in range(m):
                X += xyz[idx[i]][0]
                Y += xyz[idx[i]][1]
                Z += xyz[idx[i]][2]
            score = max(score, abs(X)+abs(Y)+abs(Z))

print(score)

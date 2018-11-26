# -*- coding: utf-8 -*-

sx,sy,tx,ty = map(int, input().split())

res = []

for _ in range(sx,tx):
    res.append("R")
for _ in range(sy,ty):
    res.append("U")
for _ in range(sx,tx):
    res.append("L")
for _ in range(sy,ty):
    res.append("D")
res.append("D")
for _ in range(sx,tx):
    res.append("R")
res.append("R")
for _ in range(sy,ty):
    res.append("U")
res.append("ULU")
for _ in range(sx,tx):
    res.append("L")
res.append("L")
for _ in range(sy,ty):
    res.append("D")
res.append("DR")

print("".join(res))

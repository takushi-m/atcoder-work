# -*- coding: utf-8 -*-
line = input().split(" ")
sx = int(line[0])
sy = int(line[1])
tx = int(line[2])
ty = int(line[3])

ret = []
# s->t
for _ in range(tx-sx):
    ret.append("R")
for _ in range(ty-sy):
    ret.append("U")

# t->s
for _ in range(tx-sx):
    ret.append("L")
for _ in range(ty-sy):
    ret.append("D")

# s->t
ret.append("D")
for _ in range(tx-sx+1):
    ret.append("R")
for _ in range(ty-sy+1):
    ret.append("U")
ret.append("L")

# t->s
ret.append("U")
for _ in range(tx-sx+1):
    ret.append("L")
for _ in range(ty-sy+1):
    ret.append("D")
ret.append("R")

print("".join(ret))

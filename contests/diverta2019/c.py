# -*- coding: utf-8 -*-
n = int(input())
sl = [input() for _ in range(n)]

xa = []
bx = []
ba = []
x = []
for s in sl:
    if s[0]=="B" and s[-1]=="A":
        ba.append(s)
    elif s[-1]=="A":
        xa.append(s)
    elif s[0]=="B":
        bx.append(s)
    else:
        x.append(s)

if len(xa)>0:
    xa = xa[:-1]+[xa[-1]+"".join(ba)]
elif len(bx)>0:
    bx = bx[:-1]+["".join(ba)+bx[-1]]
else:
    x.append("".join(ba))

if len(xa)>=len(bx):
    for i in range(len(bx)):
        x.append(xa[i]+bx[i])
    x = x+xa[len(bx):]
else:
    for i in range(len(xa)):
        x.append(xa[i]+bx[i])
    x = x+bx[len(xa):]

res = "".join(x)
print(res.count("AB"))

# -*- coding: utf-8 -*-
s = input()

cp = 0
cg = 0

for ss in list(s):
    if ss == "p":
        cp += 1
    else:
        cg += 1

if cg==cp:
    print(0)
else:
    print((cg+cp)//2 - cp)

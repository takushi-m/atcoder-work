# -*- coding: utf-8 -*-
s = input()

res1 = 0
res2 = 0
f1 = "0"
f2 = "1"
for c in s:
    if f1!=c:
        res1 += 1
    if f2!=c:
        res2 += 1

    if f1=="0":
        f1 = "1"
    else:
        f1 = "0"
    if f2=="0":
        f2 = "1"
    else:
        f2 = "0"

print(min(res1,res2))

# -*- coding: utf-8 -*-
n,k = map(int, input().split())
s = input()

il = [0]

for i in range(1,n):
    if s[i]!=s[i-1]:
        il.append(i)

res = -1
for i in range(len(il)):
    if s[il[i]]=="0":
        ri = i+2*k
    else:
        ri = i+2*k+1

    if ri>=len(il):
        r = n
    else:
        r = il[ri]
    res = max(res, r-il[i])

print(res)

# -*- coding: utf-8 -*-
n = int(input())
wl = [int(input()) for _ in range(n)]

l = [wl[0]]
for w in wl[1:]:
    l.sort()
    add = False
    for i in range(len(l)):
        if l[i]>=w:
            l[i] = w
            add = True
            break
    if not add:
        l.append(w)

print(len(l))
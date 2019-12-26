# -*- coding: utf-8 -*-
s = input()
n = len(s)
l = [1]*n

i = 0
while i<n:
    if s[i]=="R":
        j = i
        e,o = 0,0
        while s[j]=="R":
            o += l[j]
            l[j] = 0
            e,o = o,e
            j += 1
        l[j-1] += e
        l[j] += o

        i = j
    i += 1
# print(*l)

i = n-1
while i>=0:
    if s[i]=="L":
        j = i
        e,o = 0,0
        while s[j]=="L":
            o += l[j]
            l[j] = 0
            e,o = o,e
            j -= 1
        l[j+1] += e
        l[j] += o

        i = j
    i -= 1
print(*l)
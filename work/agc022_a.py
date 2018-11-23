# -*- coding: utf-8 -*-
s = input()
x = list("abcdefghijklmnopqrstuvwxyz")

if len(s)<26:
    for c in x:
        if c not in s:
            print(s+c)
            exit()
else:
    s = list(s)
    d = set()
    c = s[-1]
    d.add(c)
    i = len(s)-2
    while True:
        if i<0:
            break
        elif s[i]>c:
            c = s[i]
            i -= 1
            d.add(c)
        else:
            break
    if i>=0:
        minc = None
        for c in d:
            if c<s[i]:
                continue
            elif minc is None:
                minc = c
            elif c<minc:
                minc = c
        if minc is not None:
            s[i] = minc
            s = s[:i+1]
            print("".join(s))
            exit()
print(-1)

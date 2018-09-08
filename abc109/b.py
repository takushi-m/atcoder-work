# -*- coding: utf-8 -*-
n = int(input())
d = [input()]

ret = "Yes"
for _ in range(n-1):
    w = input()
    if w[0]!=d[-1][-1] or w in d:
        ret = "No"
    d.append(w)

print(ret)

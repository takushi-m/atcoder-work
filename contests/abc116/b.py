# -*- coding: utf-8 -*-
s = int(input())
d = {s:1}
before = s
i = 1

def f(n):
    if n%2==0:
        return n//2
    else:
        return 3*n+1

while True:
    i += 1
    ai = f(before)
    if ai in d:
        res = i
        break
    else:
        d[ai] = i
        before = ai

# print(d)
print(res)

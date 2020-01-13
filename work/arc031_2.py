# -*- coding: utf-8 -*-
from collections import deque
m = [input() for _ in range(10)]

def dfs(shi,swi):
    c = [list(m[i]) for i in range(10)]
    q = deque([(shi,swi)])

    while len(q)>0:
        chi,cwi = q.pop()
        c[chi][cwi] = "x"

        for hi,wi in [[chi+1,cwi],[chi,cwi+1],[chi-1,cwi],[chi,cwi-1]]:
            if hi<0 or hi>=10 or wi<0 or wi>=10:
                continue
            if c[hi][wi]=="x":
                continue
            q.append((hi,wi))

    for hi in range(10):
        for wi in range(10):
            if c[hi][wi]=="o":
                return False
    return True

for hi in range(10):
    for wi in range(10):
        if dfs(hi,wi):
            print("YES")
            exit()
print("NO")
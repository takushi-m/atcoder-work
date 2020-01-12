# -*- coding: utf-8 -*-
from collections import deque
h,w = map(int, input().split())
s = [input() for _ in range(h)]

if h==1 and w==1:
    print(0)
    exit()

maxr = 0
for hi in range(h):
    for wi in range(w):
        if s[hi][wi]==".":
            maxr += 1

def solve(sh,sw):
    res = -1
    visited = [[False for _ in range(w)] for _ in range(h)]
    visited[sh][sw] = True
    q = deque([(sh,sw,0)])
    while len(q)>0:
        hi,wi,r = q.popleft()
        for dh,dw in [[1,0],[0,1],[-1,0],[0,-1]]:
            if hi+dh>=0 and hi+dh<h and wi+dw>=0 and wi+dw<w and s[hi+dh][wi+dw]==".":
                if not visited[hi+dh][wi+dw]:
                    visited[hi+dh][wi+dw] = True
                    q.append((hi+dh,wi+dw,r+1))
                    res = max(res, r+1)

    return res

res = -1
for shi in range(h):
    for swi in range(w):
        if s[shi][swi]=="#":
            continue
        r = solve(shi,swi)
        res = max(res, r)

print(res)
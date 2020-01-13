# -*- coding: utf-8 -*-
from collections import deque

h,w = map(int, input().split())
m = [input() for _ in range(h)]

def start():
    for hi in range(h):
        for wi in range(w):
            if m[hi][wi]=="s":
                return hi,wi

shi,swi = start()
visited = [[False for _ in range(w)] for _ in range(h)]
q = deque([(shi,swi)])

while len(q):
    chi,cwi = q.pop()
    visited[chi][cwi] = True
    for hi,wi in [[chi+1,cwi],[chi,cwi+1],[chi-1,cwi],[chi,cwi-1]]:
        if hi<0 or hi>=h or wi<0 or wi>=w:
            continue

        if m[hi][wi]=="g":
            print("Yes")
            exit()

        if m[hi][wi]=="." and not visited[hi][wi]:
            q.append((hi,wi))

print("No")
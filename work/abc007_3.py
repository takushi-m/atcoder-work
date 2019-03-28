# -*- coding: utf-8 -*-
import queue
h,w = map(int, input().split())
sh,sw = map(int, input().split())
sh -= 1
sw -= 1
gh,gw = map(int, input().split())
gh -= 1
gw -= 1

d = []
for _ in range(h):
    d.append(input())

cost = [[0]*w for _ in range(h)]

q = queue.Queue()
q.put((sh,sw))
while not q.empty():
    hi,wi = q.get()
    if gh==hi and gw==wi:
        break

    for dh,dw in [[1,0],[0,1],[-1,0],[0,-1]]:
        if h>dh+hi>=0 and w>dw+wi>=0 and d[dh+hi][dw+wi]==".":
            if cost[dh+hi][dw+wi]==0:
                cost[dh+hi][dw+wi] = cost[hi][wi]+1
                q.put((dh+hi,dw+wi))
            elif cost[dh+hi][dw+wi]>cost[hi][wi]+1:
                cost[dh+hi][dw+wi] = cost[hi][wi]+1
                q.put((dh+hi,dw+wi))

print(cost[gh][gw])

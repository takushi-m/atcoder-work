# -*- coding: utf-8 -*-
from collections import deque
h,w = map(int, input().split())
sh,sw = map(int, input().split())
gh,gw = map(int, input().split())

m = ["#"*w] + ["#"+input()+"#" for _ in range(h)] + ["#"*w]

dist = [[10**9]*w for _ in range(h)]
dist[sh][sw] = 0
q = deque([(sh,sw)])

while len(q):
    ch,cw = q.popleft()
    r = dist[ch][cw]
    
    for hi,wi in [[ch+1,cw],[ch,cw+1],[ch-1,cw],[ch,cw-1]]:
        if m[hi][wi]=="." and dist[hi][wi]>r+1:
            dist[hi][wi] = r+1
            q.append((hi,wi))

print(dist[gh][gw])
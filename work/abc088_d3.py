# -*- coding: utf-8 -*-
from collections import deque
h,w = map(int, input().split())
m = ["#"*(w+2)] + ["#"+input()+"#" for _ in range(h)] + ["#"*(w+2)]

cnt = 0
for hi in range(1,h+1):
    for wi in range(1,w+1):
        if m[hi][wi]==".":
            cnt += 1

inf = 10**9
d = [[inf]*(w+2) for _ in range(h+2)]
q = deque([(1,1,1)])
d[1][1] = 1
while len(q):
    ch,cw,r = q.popleft()

    for hi,wi in [[ch+1,cw],[ch,cw+1],[ch-1,cw],[ch,cw-1]]:
        if m[hi][wi]=="." and d[hi][wi]>r+1:
            d[hi][wi]=r+1
            q.append((hi,wi,r+1))

if d[h][w]==inf:
    print(-1)
else:
    print(cnt-d[h][w])
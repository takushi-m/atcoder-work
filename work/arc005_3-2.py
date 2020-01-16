# -*- coding: utf-8 -*-
from collections import deque
h,w = map(int, input().split())
m = [list(input()) for _ in range(h)]

for hi in range(h):
    for wi in range(w):
        if m[hi][wi]=="s":
            sh = hi
            sw = wi

inf = 10**9
d = [[inf]*w for _ in range(h)]
d[sh][sw] = 0
q = deque([(sh,sw)])
while len(q)>0:
    ch,cw = q.popleft()
    c = d[ch][cw]

    for hi,wi in [[ch+1,cw],[ch,cw+1],[ch-1,cw],[ch,cw-1]]:
        if not (h>hi>=0 and w>wi>=0):
            continue

        if m[hi][wi]==".":
            if d[hi][wi]>c:
                d[hi][wi] = c
                q.append((hi,wi))
        elif m[hi][wi]=="#":
            if d[hi][wi]>c+1 and 2>=c+1:
                d[hi][wi] = c+1
                q.append((hi,wi))
        elif m[hi][wi]=="g":
            if 3>=c+1:
                print("YES")
                exit()
print("NO")
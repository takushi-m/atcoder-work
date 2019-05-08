# -*- coding: utf-8 -*-
h,w = map(int, input().split())
al = [list(input()) for _ in range(h)]
cnt = 0

q = []
for hi in range(h):
    for wi in range(w):
        if al[hi][wi]=="#":
            q.append((hi,wi))

while len(q)>0:
    nq = []
    cnt += 1
    for hi,wi in q:
        for d in [[1,0],[0,1],[-1,0],[0,-1]]:
            if h>hi+d[0]>=0 and w>wi+d[1]>=0:
                if al[hi+d[0]][wi+d[1]]==".":
                    al[hi+d[0]][wi+d[1]] = "#"
                    nq.append((hi+d[0], wi+d[1]))
    q = nq

print(cnt-1)

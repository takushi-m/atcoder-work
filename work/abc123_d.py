# -*- coding: utf-8 -*-
import heapq
x,y,z,k = map(int, input().split())
al = list(map(int, input().split()))
bl = list(map(int, input().split()))
cl = list(map(int, input().split()))

al.sort(reverse=True)
bl.sort(reverse=True)
cl.sort(reverse=True)
regist = set()
regist.add((0,0,0))
q = [(-1*(al[0]+bl[0]+cl[0]),0,0,0)]
heapq.heapify(q)
for _ in range(k):
    s,ai,bi,ci = heapq.heappop(q)
    print(-s,flush=True)

    if ai+1<x and (ai+1,bi,ci) not in regist:
        heapq.heappush(q, (-1*(al[ai+1]+bl[bi]+cl[ci]), ai+1,bi,ci))
        regist.add((ai+1,bi,ci))

    if bi+1<y and (ai,bi+1,ci) not in regist:
        heapq.heappush(q, (-1*(al[ai]+bl[bi+1]+cl[ci]), ai,bi+1,ci))
        regist.add((ai,bi+1,ci))

    if ci+1<z and (ai,bi,ci+1) not in regist:
        heapq.heappush(q, (-1*(al[ai]+bl[bi]+cl[ci+1]), ai,bi,ci+1))
        regist.add((ai,bi,ci+1))

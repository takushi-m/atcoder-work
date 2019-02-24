# -*- coding: utf-8 -*-
from bisect import bisect_left
INF = 10**18
a,b,q = map(int, input().split())
sl = [-INF] + [int(input()) for _ in range(a)] + [INF]
tl = [-INF] + [int(input()) for _ in range(b)] + [INF]
# print(sl)
# print(tl)
for _ in range(q):
    x = int(input())
    si = bisect_left(sl,x)
    ti = bisect_left(tl,x)
    # print(x,si,ti)
    res = INF
    for s in [sl[si-1], sl[si]]:
        for t in [tl[ti-1], tl[ti]]:
            res = min(
                res,
                abs(s-x)+abs(t-s),
                abs(t-x)+abs(s-t)
            )
    print(res)

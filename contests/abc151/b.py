# -*- coding: utf-8 -*-
n,k,m = map(int, input().split())
al = list(map(int, input().split()))

s = sum(al)
if m*n<=s:
    print(0)
else:
    if m*n-s>k:
        print(-1)
    else:
        print(m*n-s)
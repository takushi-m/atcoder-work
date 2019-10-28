# -*- coding: utf-8 -*-
n = int(input())
dl = list(map(int, input().split()))
dl = sorted(dl)

if n%2==0:
    x = dl[n//2-1]
    y = dl[n//2]
    print(y-x)
else:
    print(0)
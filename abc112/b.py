# -*- coding: utf-8 -*-
N,T = map(int,input().split())

ret = 10**5
for _ in range(N):
    c,t = map(int, input().split())
    if t<=T:
        ret = min(ret, c)

if ret==10**5:
    print("TLE")
else:
    print(ret)

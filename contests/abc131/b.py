# -*- coding: utf-8 -*-
n,l = map(int, input().split())

s = 0
for i in range(1,n+1):
    s += l+i-1

ans = 10**6
idx = -1
for i in range(1,n+1):
    s2 = s - (l+i-1)
    if abs(s-s2)<ans:
        ans = abs(s-s2)
        idx = i

print(s-(l+idx-1))

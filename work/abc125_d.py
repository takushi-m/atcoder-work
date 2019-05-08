# -*- coding: utf-8 -*-

n = int(input())
al = list(map(int, input().split()))

m = 10**10
c = 0
s = 0
for a in al:
    m = min(m, abs(a))
    s += abs(a)
    if a<0:
        c += 1

if c%2==0:
    print(s)
else:
    print(s-2*m)

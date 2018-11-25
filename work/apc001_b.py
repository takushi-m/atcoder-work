# -*- coding: utf-8 -*-
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

p1 = 0
p2 = 0
ng = 0
for i in range(n):
    if b[i]>=a[i]:
        p1 += (b[i]-a[i])//2
        p2 += (b[i]-a[i])%2
    else:
        ng += a[i]-b[i]

if p1>=ng:
    print("Yes")
else:
    print("No")

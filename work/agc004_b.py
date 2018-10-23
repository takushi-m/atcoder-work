# -*- coding: utf-8 -*-
n,x = map(int, input().split())
a = [int(i) for i in input().split()]
b = [a[i] for i in range(n)]

ret = sum(a)
for k in range(n):
    for i in range(n):
        b[i] = min(b[i], a[(i+n-k)%n])
    ret = min(ret, k*x+sum(b))
print(ret)

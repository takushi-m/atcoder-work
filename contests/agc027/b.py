# -*- coding: utf-8 -*-
n,X = map(int, input().split())
x = [int(n) for n in input().split()]

ret = (n+1)*X # 全部のゴミを拾って、捨てる
ret += x[-1]

for i in range(1,n):
    ret += (x[-i]-x[-i-1])*((i+1)**2)
ret += x[0]*((n+1)**2)
print(ret)

1000000000
19999999983

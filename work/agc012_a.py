# -*- coding: utf-8 -*-
n = int(input())
a = sorted(list(map(int, input().split())), reverse=True)
res = 0
for i in range(n):
    res += a[2*i+1]
print(res)

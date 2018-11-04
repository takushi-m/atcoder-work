# -*- coding: utf-8 -*-
n = int(input())
t,a = map(int, input().split())
h = [int(x) for x in input().split()]

def temp(x):
    return t - x*0.006

ret = -1
diff = 10**5
for i in range(n):
    ht = temp(h[i])
    if abs(a-ht)<diff:
        diff = abs(a-ht)
        ret = i+1
print(ret)

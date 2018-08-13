# -*- coding: utf-8 -*-

n = int(input())

def cntd(x):
    digits = 0

    while x/10>0:
        x = x//10
        digits += 1
    return digits

ret = cntd(n)
i = 1
while i**2<=n:
    if n%i==0:
        a = cntd(i)
        b = cntd(n//i)
        cur = max(a,b)
        if ret>cur:
            ret = cur
    i += 1

print(ret)

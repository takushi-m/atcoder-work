# -*- coding: utf-8 -*-
n = int(input())

def div2(x):
    ret = 0
    while x%2==0:
        x /= 2
        ret += 1
    return ret

ret = 0
for a in input().split(" "):
    a = int(a)
    ret += div2(a)

print(ret)

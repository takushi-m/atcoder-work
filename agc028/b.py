# -*- coding: utf-8 -*-
n = int(input())
suma = sum(list(map(int , input().split())))

def fact(x):
    ret = 1
    for i in range(1,x+1):
        ret *= i
    return ret

ret = 0
for i in range(n):
    ret += suma*fact(n)//(i+1)
print(ret)

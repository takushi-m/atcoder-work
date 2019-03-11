# -*- coding: utf-8 -*-
a,b = map(int, input().split())

def g(x):
    if x%2==1:
        return ((x+1)//2)%2
    else:
        return ((x//2)%2)^x

def f(a,b):
    return g(b) ^ g(a-1)

print(f(a,b))

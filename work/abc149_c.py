# -*- coding: utf-8 -*-
from math import sqrt
x = int(input())

def prime(n):
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return True

for i in range(x,10**6):
    if prime(i):
        print(i)
        exit()
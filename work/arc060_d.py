# -*- coding: utf-8 -*-
import math
n = int(input())
s = int(input())

if s==n:
    print(n+1)
    exit()

def f(b,n):
    ret = 0
    while n>=b:
        ret += n%b
        n = n//b
    return ret+n

b = 2
while b*b<n:
    if f(b,n)==s:
        print(b)
        exit()
    b += 1

p = math.ceil(math.sqrt(n))+1
while p>0:
    q = s - p
    b = (n-q)//p
    if b>0 and f(b,n)==s:
        print(b)
        exit()
    p -= 1
print(-1)

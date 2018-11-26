# -*- coding: utf-8 -*-
import math
n = int(input())

if n==1:
    print(1)
    exit()
primes = []
x = 2
while x*x<=n:
    if n%x==0:
        primes.append(x)
        primes.append(n//x)
    x += 1

# print(primes)

def digit(x):
    return math.ceil(math.log10(x)) + (1 if x%10==0 else 0)

res = digit(n)
for i in range(len(primes)):
    a = primes[i]
    b = n//a
    t = max(digit(a), digit(b))
    # print(a,b,t)
    res = min(res, t)

print(res)

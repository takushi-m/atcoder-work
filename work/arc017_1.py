# -*- coding: utf-8 -*-
n = int(input())

def isPrime(x):
    if x%2==0:
        return False
    a = 3
    while x>=a*a:
        if x%a==0:
            return False
        a += 2
    return True

if isPrime(n):
    print("YES")
else:
    print("NO")
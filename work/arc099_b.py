# -*- coding: utf-8 -*-

def S(n):
    res = 0
    while n>0:
        res += n%10
        n //= 10
    return res

def check(n):
    for m in range(n+1,10**7):
        if n/S(n)>m/S(m):
            return False
    return True

print(S(2))
print(S(3))
print(check(2))

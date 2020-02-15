# -*- coding: utf-8 -*-
n = int(input())

def sieve(n):
    res = list(range(n+10)) # nが小さい時よう
    res[0] = -1
    res[1] = -1
    i = 2
    while i*i<n:
        if res[i]<i:
            i += 1
            continue
        j = i*i
        while j<n:
            if res[j]==j:
                res[j] = i
            j += i
        i += 1
    return res

res = sieve(n)
r = 0
for i in range(2,n):
    if res[i]==i:
        r += 1
print(r)
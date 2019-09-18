# -*- coding: utf-8 -*-
import string

atoi = {}
for i in range(len(string.ascii_lowercase)):
    atoi[string.ascii_lowercase[i]] = i

b = 1007
h = 10**9+7
hash = [0]*(10**4)
power = [1]*(10**4)
def rh(s):
    n = len(s)
    for i in range(n):
        hash[i+1] = (hash[i]*b + atoi[s[i]])
        power[i+1] = power[i]*b

def get(l,r):
    return (hash[r] - hash[l]*power[r-l] + h)%h

n = int(input())
s = input()

rh(s)

d = {}
res = 0
for i in range(n):
    for j in range(i+1,n+1):
        hh = get(i,j)
        if hh not in d:
            d[hh] = i
        else:
            res = max(res, min(i-d[hh],j-i))

print(res)

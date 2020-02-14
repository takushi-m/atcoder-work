# -*- coding: utf-8 -*-
# GCD
def gcd(a,b):
    while b!=0:
        a,b = b,a%b
    return a

# lのGCD
def gcdlist(l):
    res = l[0]
    for i in range(1,len(l)):
        res = gcd(res, l[i])
    return res


n,k = map(int, input().split())
al = list(map(int, input().split()))

m = gcdlist(al)
al.sort(reverse=True)

for a in al:
    if a>k:
        if (a-k)%m==0:
            print("POSSIBLE")
            exit()
    elif a==k:
        print("POSSIBLE")
        exit()
    else:
        break
print("IMPOSSIBLE")

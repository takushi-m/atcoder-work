# -*- coding: utf-8 -*-
n,m = map(int, input().split())
s = input()
t = input()

def gcd(a,b):
    if a<b:
        a,b = b,a
    if b==0:
        return a
    c = a%b
    return gcd(b,c)

def lcm(a,b):
    return a*b//gcd(a,b)

l = lcm(n,m)

for i in range(n):
    if i*m%n==0:
        j = i*m//n
        if s[i]!=t[j]:
            print(-1)
            exit()
print(l)

# for i in range(n):
#     ls[i*l//n] = s[i]
# for i in range(m):
#     if ls[i*l//m]!="." and ls[i*l//m]!=t[i]:
#         print(-1)
#         exit()
# print(l)

# coding=utf-8
import math

line = input().split(" ")
n = int(line[0])
m = int(line[1])

def perm(x):
    return math.factorial(x)

p = 10**9 + 7

f = 1
if n==m:
    f = 2

if abs(n-m)>1:
    print(0)
else:
    print(f*perm(n)*perm(m)%p)

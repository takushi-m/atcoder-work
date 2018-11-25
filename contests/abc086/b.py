# coding=utf-8
from math import sqrt

line = input().split(" ")
n = int(line[0]+line[1])

a = int(sqrt(n))

if a*a==n:
    print("Yes")
else:
    print("No")

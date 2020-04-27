from math import sqrt,ceil
x = int(input())
t = 1
while t*(t+1)//2<x:
    t += 1
print(t)
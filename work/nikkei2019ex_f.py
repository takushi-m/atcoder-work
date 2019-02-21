# -*- coding: utf-8 -*-
n = int(input())

def f(x):
    res = ""
    if x%2==0:
        res += "a"
    if x%3==0:
        res += "b"
    if x%4==0:
        res += "c"
    if x%5==0:
        res += "d"
    if x%6==0:
        res += "e"
    if res=="":
        res = str(x)
    return res

for i in range(1,n+1):
    print(f(i))

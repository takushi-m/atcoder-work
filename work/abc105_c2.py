# -*- coding: utf-8 -*-
n = int(input())
if n==0:
    print(0)
    exit()
s = []

while n != 0:
    x = n%-2
    if x<0:
        s.append("1")
        n = n//-2 +1
    else:
        s.append("0")
        n = n//-2
s.reverse()
print("".join(s))

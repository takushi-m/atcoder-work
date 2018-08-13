# -*- coding: utf-8 -*-

line = input().split(" ")
a = int(line[0])
b = int(line[1])

if a*b==15:
    print("*")
elif a+b==15:
    print("+")
else:
    print("x")

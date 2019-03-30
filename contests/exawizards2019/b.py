# -*- coding: utf-8 -*-
n = int(input())
s = input()
b = 0
r = 0
for c in list(s):
    if c=="R":
        r += 1
    else:
        b += 1

if r>b:
    print("Yes")
else:
    print("No")

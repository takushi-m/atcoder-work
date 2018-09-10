# -*- coding: utf-8 -*-
n = input()
s = input()
num = 0
l = 0
for c in s:
    if c=="(":
        num += 1
    else:
        if num>0:
            num -= 1
        else:
            l += 1
r = num

print("("*l+s+")"*r)

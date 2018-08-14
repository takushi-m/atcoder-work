# -*- coding: utf-8 -*-
from math import ceil
n = int(input())

ret = ""

while n!=0:
    r = ceil(n/-2)
    if n!=r*-2:
        ret += "1"
    else:
        ret += "0"
    n = r

if ret=="":
    print("0")
else:
    print(ret[::-1])

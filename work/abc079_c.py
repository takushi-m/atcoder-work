# -*- coding: utf-8 -*-

line = list(input())
a = int(line[0])
b = int(line[1])
c = int(line[2])
d = int(line[3])

op = ["+", "-"]

for op1 in op:
    for op2 in op:
        for op3 in op:
            ret = a
            if op1=="+":
                ret += b
            else:
                ret -= b
            if op2=="+":
                ret += c
            else:
                ret -= c
            if op3=="+":
                ret += d
            else:
                ret -= d
            if ret==7:
                print(a,op1,b,op2,c,op3,d,"=7",sep="")
                exit()

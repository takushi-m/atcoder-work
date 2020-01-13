# -*- coding: utf-8 -*-
a,b,c,d = list(input())

for op1 in ["+","-"]:
    for op2 in ["+","-"]:
        for op3 in ["+","-"]:
            s = a+op1+b+op2+c+op3+d
            r = eval(s)
            if r==7:
                print(s+"=7")
                exit()
# -*- coding: utf-8 -*-
a,b,c,d = map(int, list(input()))

for op1 in ["+","-"]:
    for op2 in ["+","-"]:
        for op3 in ["+","-"]:
            res = 0
            if op1=="+":
                res += a+b
            else:
                res += a-b
            if op2=="+":
                res += c
            else:
                res -= c
            if op3=="+":
                res += d
            else:
                res -= d
            if res==7:
                print("".join([str(a),op1,str(b),op2,str(c),op3,str(d),"=7"]))
                exit()

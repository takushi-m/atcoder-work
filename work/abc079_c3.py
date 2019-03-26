# -*- coding: utf-8 -*-
x = list(map(int, list(input())))
op = ["-","+"]
for i in range(8):
    t = x[0]
    for j in range(3):
        if i>>j&1 == 1:
            t += x[j+1]
        else:
            t -= x[j+1]
    if t==7:
        print("{}{}{}{}{}{}{}=7".format(
            x[0],op[i>>0&1],x[1],op[i>>1&1],x[2],op[i>>2&1],x[3]
        ))
        break

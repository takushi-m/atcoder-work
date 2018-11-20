# -*- coding: utf-8 -*-
n = int(input())
res = 1
cur = None
np = None
for a in list(map(int, input().split())):
    # print(res,cur,np,a)
    if cur is None:
        pass
    elif np is None:
        if a==cur:
            np = 0
        elif a>cur:
            np = 1
        else:
            np = -1
    else:
        if np==0:
            if a==cur:
                pass
            elif a>cur:
                np = 1
            else:
                np = -1
        elif np>0:
            if a>=cur:
                pass
            else:
                res += 1
                np = None
        else:
            if a<=cur:
                pass
            else:
                res += 1
                np = None
    cur = a

print(res)

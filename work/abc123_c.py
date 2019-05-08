# -*- coding: utf-8 -*-
from math import ceil

def f1(n,a,b,c,d,e):
    m = min(a,b,c,d,e)
    if m==1:
        s = n
    elif n>m:
        s = ceil(n/m)
    else:
        s = 1
    return 5+s-1

def f2(n,a,b,c,d,e):
    op = [a,b,c,d,e]
    l = [0]*6
    l[0] = n
    res = 0
    flag = True
    while flag:
        flag = False
        for i in [4,3,2,1,0]:
            if l[i]>0:
                m = min(op[i],l[i])
                l[i] -= m
                l[i+1] += m
                flag = True
        res += 1
        if l[5]==n:
            flag = False
    return res

if __name__ == '__main__':
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    print(f1(n,a,b,c,d,e))

    # from random import randint
    # for _ in range(100):
    #     n = randint(1,100)
    #     a = randint(1,20)
    #     b = randint(1,20)
    #     c = randint(1,20)
    #     d = randint(1,20)
    #     e = randint(1,20)
    #
    #     r1 = f1(n,a,b,c,d,e)
    #     r2 = f2(n,a,b,c,d,e)
    #     if r1!=r2:
    #         print(r1,r2)
    #         print(n,a,b,c,d,e)
    #         break

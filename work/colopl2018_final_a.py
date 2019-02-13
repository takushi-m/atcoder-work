# -*- coding: utf-8 -*-
def dmg(k):
    return k*(k+1)//2

def f(n,s):
    s2 = [c for c in s.split("B") if c != ""]

    if len(set(s))==1:
        if s[0]=="A":
            return dmg(len(s)*n)
        else:
            return 0
    if len(s2)==1:
        return dmg(len(s2[0]))*n

    res = 0
    res += dmg(len(s2[0]))
    res += dmg(len(s2[-1]))

    if len(s2[1:-1]) > 0:
        tmp = 0
        for c in s2[1:-1]:
            tmp += dmg(len(c))
        res += n*tmp

    if s[0] == "A" and s[-1] == "A":
        res += dmg(len(s2[0])+len(s2[-1]))*(n-1)
    else:
        res += dmg(len(s2[0]))*(n-1)
        res += dmg(len(s2[-1]))*(n-1)
    return res

def f2(n,s):
    res = 0
    for c in [c for c in (s*n).split("B") if c!=""]:
        res += dmg(len(c))
    return res

if __name__ == '__main__':
    n = int(input())
    s = input()
    print(f(n,s))

    # from random import randint
    # for _ in range(100):
    #     n = 10
    #     s = "".join(["AB"[randint(0,1)] for _ in range(10)])
    #     res1 = f(n,s)
    #     res2 = f2(n,s)
    #     if res1!=res2:
    #         print(n,s)
    #         print(res1)
    #         print(res2)

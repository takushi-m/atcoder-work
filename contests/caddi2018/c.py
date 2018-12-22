# -*- coding: utf-8 -*-
# n = int(input())
# al = list(map(int, input().split()))

def calc(al):
    n = len(al)
    all = [al[i] for i in range(n)]
    res = 0
    ca = al[0]
    flag = True
    for i in range(1,n):
        if ca>=all[i] and flag:
            if ca>all[i]:
                res += 1
            ca = all[i]
        else:
            flag = False
            while ca>all[i]:
                all[i] *= 4
                res += 2
            ca = all[i]

    all = [al[i] for i in range(n)]
    res2 = 0
    ca = al[0]
    flag = True
    for i in range(1,n):
        if ca>=all[i] and flag:
            pass
        else:
            flag = False
            while ca<=all[i]:
                all[i] *= -2
                res2 += 1
            ca = all[i]
    res2 += n-1

    return min(res,res2)

def f(al):
    n = len(al)
    res = calc(al)

    bimin = 10
    com = [0]*n
    def next(com):
        com[0] += 1
        for i in range(n-1):
            if com[i]>bimin:
                com[i] = 0
                com[i+1] += 1

    def check(com):
        rl = [al[i]*((-2)**com[i]) for i in range(n)]

        for i in range(1,n):
            if rl[i-1]>rl[i]:
                return False
        return True

    res2 = (bimin+1)**n
    comres = []
    for _ in range((bimin+1)**n):
        if check(com):
            if res2>sum(com):
                comres = [com[i] for i in range(n)]
            res2 = min(res2, sum(com))
        next(com)

    if res!=res2:
        print(res, res2, al, comres)
    return res==res2



from random import randrange
n = 4
for _ in range(10):
    al = [randrange(1,100) for _ in range(n)]
    f(al)
f([2,1,1,3])

# -*- coding: utf-8 -*-
from math import sqrt, exp
from random import randint, shuffle, random
import time
from pprint import pprint
n = -1
xy = []

def dis(i,j):
    return (xy[i][0]-xy[j][0])**2 + (xy[i][1]-xy[j][1])**2

def score(path):
    d = []
    for i in range(n-1):
        d.append(dis(path[i],path[i+1]))
    d.append(dis(path[n-1],path[0]))
    avg = sum(d)/n
    return sum([(d[i]-avg)**2 for i in range(n)])

def next_p(s,s2,itr,init):
    if itr<1000:
        beta = 0.1
    else:
        beta = 0.1*init**itr
    # print(beta)
    if s>=s2:
        return 1
    else:
        delta = s - s2
        if delta*beta>100:
            return 1
        elif delta*beta<100:
            return 0
        else:
            return exp(delta*beta)

def fun(init):
    start = time.time()
    res = [i for i in range(n)]
    shuffle(res)
    s = score(res)
    idx = 1
    while (time.time()-start)<1.95:
        i = randint(0,199)
        j = randint(0,199)
        if abs(i-j)<=1:
            continue

        res[(i+1)%n],res[(j+1)%n] = res[(j+1)%n],res[(i+1)%n]
        s2 = score(res)
        if next_p(s,s2,idx,init)>random():
            s = s2
            # print(s)
        else:
            # 戻す
            res[(i+1)%n],res[(j+1)%n] = res[(j+1)%n],res[(i+1)%n]
        idx += 1
    return s,res


if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        x,y = map(int, input().split())
        xy.append((x,y))


    # init = 1.01
    # for i in range(1,10+1):
    #     print(init**i, fun(init**i)[0]/10**10)
    s,res = fun(1.01)
    for r in res:
        print(r)

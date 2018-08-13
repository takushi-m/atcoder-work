# coding=utf-8
from functools import lru_cache

line = input().split(" ")
H = int(line[0])
W = int(line[1])
A = int(line[2])
B = int(line[3])

g = [1, 1]
for i in range(2,H+W):
    g.append(g[i-1]*i)

def fac(n):
    if n in g:
        return g[i]
    print("calc!")
    ret = 1
    for i in range(1,n+1):
        ret *= i
    return ret

def route(_h,_w):
    h = _h-1
    w = _w-1
    ret = 1

    return fac(h+w)/(fac(w)*fac(h))

ret = 0
x = 10**9+7
for h in range(1,H-A+1):
    tmp = route(h, B)
    tmp *= route(H-h+1, W-B)

    ret = (ret+tmp)%x

print(int(ret))

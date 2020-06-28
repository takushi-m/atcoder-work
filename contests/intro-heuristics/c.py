from random import randint
from functools import lru_cache

D = int(input())
cl = list(map(int, input().split()))
sl = [list(map(int, input().split())) for _ in range(D)]
tl = [int(input()) for _ in range(D)]
M = int(input())
dq = [list(map(int, input().split())) for _ in range(M)]

@lru_cache(maxsize=10**5)
def score(d, ti, *last):
    s = sl[d-1][ti]
    for i in range(len(cl)):
        c = cl[i]
        s -= c*(d-last[i])
    return s

def scores(tl):
    s = 0
    last = [0]*26
    for d in range(D):
        t = tl[d] - 1
        last[t] = d+1
        s += score(d+1,t,*last)
    return s


for i in range(M):
    d,q = dq[i]
    x = tl[d-1]
    tl[d-1] = q
    print(scores(tl))


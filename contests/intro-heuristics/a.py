from random import randint

D = int(input())
cl = list(map(int, input().split()))
sl = [list(map(int, input().split())) for _ in range(D)]

def score(d, ti, last):
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
        s += score(d+1,t,last)
    return s


tl = [randint(1,26) for _ in range(D)]
s = scores(tl)
for _ in range(10000):
    d = randint(1,D)
    q = randint(1,26)
    x = tl[d-1]
    tl[d-1] = q
    s2 = scores(tl)
    if s2>s:
        s = s2
    else:
        tl[d-1] = x


for t in tl:
    print(t)


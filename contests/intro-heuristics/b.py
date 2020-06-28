D = int(input())
cl = list(map(int, input().split()))
sl = [list(map(int, input().split())) for _ in range(D)]
tl = [int(input()) for _ in range(D)]

def score(d, ti, last):
    s = sl[d-1][ti]
    for i in range(len(cl)):
        c = cl[i]
        s -= c*(d-last[i])
    return s

s = 0
last = [0]*26
for d in range(D):
    t = tl[d] - 1
    last[t] = d+1
    s += score(d+1,t,last)
    print(s)


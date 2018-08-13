# coding=utf-8
line = input().split(" ")
h = int(line[0])
w = int(line[1])
d = int(line[2])

table = [0 for _ in range(h*w+1)]
for hi in range(h):
    line = list(map(int, input().split(" ")))

    for wi in range(w):
        table[line[wi]] = (hi+1, wi+1)

def calc(l,r):
    ret = 0
    if l!=r:
        c1 = table[l]
        c2 = table[r]
        ret += abs(c1[0]-c2[0])+abs(c1[1]-c2[1])
    return ret

acc = [0 for _ in range(h*w+1)]
for dd in range(1,d+1):
    s = dd+d
    while s<=h*w:
        acc[s] = calc(s-d,s)+acc[s-d]
        s += d

q = int(input())
for _ in range(q):
    line = input().split(" ")
    l = int(line[0])
    r = int(line[1])

    ret = acc[r] - acc[l]
    print(ret)

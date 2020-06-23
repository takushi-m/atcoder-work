from math import pi
n,q = map(int, input().split())
xrh = [list(map(int, input().split())) for _ in range(n)]
ab = [list(map(int, input().split())) for _ in range(q)]

for a,b in ab:
    s = 0.0
    for i in range(n):
        x,r,h = xrh[i]
        if x+h<a or b<x:
            continue

        ah = h - max(0,a-x)
        ar = r/h*ah
        s += ar*ar*pi*ah/3

        bh = max(0, x+h-b)
        br = r/h*bh
        s -= br*br*pi*bh/3
    print(s)

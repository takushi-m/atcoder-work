# -*- coding: utf-8 -*-

def rev(n):
    res = 0
    while n>0:
        res = 10*res + n%10
        n = n//10
    return res

def next(x,y):
    if x<y:
        x = rev(x)
    else:
        y = rev(y)

    if x<y:
        y = y-x
    else:
        x = x-y

    return x,y

n,m = map(int, input().split())

CHECK = 1
STOP = 2
LOOP = 3

status = [[0]*1000 for _ in range(1000)]

for _x in range(1,n+1):
    for _y in range(1,m+1):
        x,y = _x,_y
        isloop = False
        l = []
        while status[x][y] == 0:
            l.append((x,y))
            status[x][y] = CHECK
            x,y = next(x,y)
            if x==0 or y==0 or status[x][y]==STOP:
                l.append((x,y))
                break
            elif status[x][y] in (CHECK,LOOP):
                l.append((x,y))
                isloop = True
                break

        if isloop:
            s = LOOP
        else:
            s = STOP

        for (x,y) in l:
            status[x][y] = s

cnt = 0
for x in range(1,n+1):
    for y in range(1,m+1):
        if status[x][y]==LOOP:
            cnt += 1
print(cnt)

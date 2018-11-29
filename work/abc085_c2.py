# -*- coding: utf-8 -*-
n,y = map(int, input().split())

for a in range(min(n,y//10000)+1):
    for b in range(min(n-a,(y-a*10000)//5000)+1):
        if a*10000+b*5000>y:
            continue
        c = (y-a*10000-b*5000)//1000
        if a+b+c==n and 10000*a+5000*b+1000*c==y:
            print(a,b,c)
            exit()
print(-1,-1,-1)

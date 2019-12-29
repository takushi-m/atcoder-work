# -*- coding: utf-8 -*-
n,a,b = map(int, input().split())

if (b-a)%2==0:
    print((b-a)//2)
else:
    r1 = a-1 + 1 + (b-a)//2
    r2 = n-b + 1 + (b-a)//2
    print(min(r1,r2))
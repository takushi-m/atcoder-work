# -*- coding: utf-8 -*-
a,b,c,k = map(int,input().split())

if k%2==0:
    if a-b>10**18:
        print("Unfair")
    else:
        print(a-b)
else:
    if b-a>10**18:
        print("Unfair")
    else:
        print(b-a)

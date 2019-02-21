# -*- coding: utf-8 -*-
N = int(input())

for n in range(1,3500+1):
    for h in range(1,3500+1):
        if (4*h*n-N*n-N*h)>0 and (N*h*n)%(4*h*n-N*n-N*h)==0:
            w = (N*h*n)//(4*h*n-N*n-N*h)
            print(h,n,w)
            exit()

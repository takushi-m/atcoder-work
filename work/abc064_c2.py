# -*- coding: utf-8 -*-
n = int(input())
a = list(map(int, input().split()))
over = 0
rate = set()
for x in a:
    if 399>=x>=1:
        rate.add(1)
    elif 799>=x>=400:
        rate.add(2)
    elif 1199>=x>=800:
        rate.add(3)
    elif 1599>=x>=1200:
        rate.add(4)
    elif 1999>=x>=1600:
        rate.add(5)
    elif 2399>=x>=2000:
        rate.add(6)
    elif 2799>=x>=2400:
        rate.add(7)
    elif 3199>=x>=2800:
        rate.add(8)
    else:
        over += 1

if len(rate)>0:
    print(len(rate),len(rate)+over)
else:
    print(1,over)

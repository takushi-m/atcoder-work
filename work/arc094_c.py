# -*- coding: utf-8 -*-
a,b,c = sorted([int(x) for x in input().split()])
ret = (c-a)//2 + (c-b)//2
a = a + 2*((c-a)//2)
b = b + 2*((c-b)//2)

if a==b and b==c:
    print(ret)
elif a<c and b<c:
    print(ret+1)
else:
    print(ret+2)

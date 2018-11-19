# -*- coding: utf-8 -*-
n = int(input())
a = list(map(int, input().split()))

o = 0
e = 0
for x in a:
    if x%2==0:
        e += 1
    else:
        o += 1

e += (o//2)
o %= 2

if o==0 and e>0:
    print("YES")
elif o==1 and e==0:
    print("YES")
else:
    print("NO")

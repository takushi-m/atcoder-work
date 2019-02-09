# -*- coding: utf-8 -*-
l = int(input())
odd = [0]
even = [0]
for i in range(l):
    a = int(input())
    if a%2==1:
        odd.append(odd[i]+1)
        even.append(even[i])
    else:
        odd.append(odd[i])
        even.append(even[i]+1)

res = 10**15
for e in range(l):
    r = even[e]-even[0]
    r += odd[l]-odd[e]
    res = min(res,r)

for e in range(l-1,-1,-1):
    r = odd[l]-odd[e]
    r += even[e]-even[0]
    res = min(res,r)

print(res)

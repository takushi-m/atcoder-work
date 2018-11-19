# -*- coding: utf-8 -*-
n,c,k = map(int, input().split())
k *= 2
t = []
for _ in range(n):
    t.append(int(input())*2)
t.sort()
# print(t)
res = 0
s = []
for x in t:
    if len(s)==0:
        s.append(x)
    else:
        # print(x,s,x-s[0])
        if x-s[0]>k:
            while len(s)>0 and x-s[0]>k:
                res += 1
                s = s[c:]
            s.append(x)
        elif len(s)+1>c:
            res += 1
            s = s[c:]
            s.append(x)
        else:
            s.append(x)
# print(s)
if len(s)>0:
    res += 1
print(res)

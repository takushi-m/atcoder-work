# -*- coding: utf-8 -*-
n = int(input())
vv = list(map(int, input().split()))
d1 = {}
d2 = {}

for i in range(n):
    v = vv[i]
    if i%2==0:
        if v not in d2:
            d2[v] = 0
        d2[v] += 1
    else:
        if v not in d1:
            d1[v] = 0
        d1[v] += 1

dl1 = sorted(list(d1.keys()), reverse=True, key=lambda k:d1[k])
dl2 = sorted(list(d2.keys()), reverse=True, key=lambda k:d2[k])
i1 = 0
i2 = 0

if len(dl1)==1 and len(dl2)==1:
    if dl1[0]==dl2[0]:
        print(n//2)
    else:
        print(0)
    exit()
elif len(dl1)==1:
    print(sum(sorted(d2.values(), reverse=True)[1:]))
    exit()
elif len(dl2)==1:
    print(sum(sorted(d1.values(), reverse=True)[1:]))
    exit()


if dl1[0]!=dl2[0]:
    res = 0
    res += sum(sorted(d1.values(), reverse=True)[1:])
    res += sum(sorted(d2.values(), reverse=True)[1:])
    print(res)
else:
    res1 = 0
    l = sorted(d1.values(), reverse=True)
    res1 += l[0]
    if len(l)>2:
        res1 += sum(l[2:])
    res1 += sum(sorted(d2.values(), reverse=True)[1:])

    res2 = 0
    l = sorted(d2.values(), reverse=True)
    res2 += l[0]
    if len(l)>2:
        res2 += sum(l[2:])
    res2 += sum(sorted(d1.values(), reverse=True)[1:])
    print(min(res1,res2))

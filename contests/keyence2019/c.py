# -*- coding: utf-8 -*-
n = int(input())
al = list(map(int, input().split()))
bl = list(map(int, input().split()))

cl = [0]*n
solved = True
for i in range(n):
    cl[i] = al[i]-bl[i]
    if cl[i]<0:
        solved = False

if solved:
    print(0)
    exit()

cl.sort(reverse=True)
# print(cl)

last = n-1
i = 0
res = 0
used = [False for _ in range(n)]
while True:
    if cl[last]>0:
        break

    while cl[i]>0 and cl[last]<0:
        if cl[i]+cl[last]>=0:
            cl[i] += cl[last]
            cl[last] = 0
            if not used[last]:
                res += 1
            used[last] = True
            last -= 1
        else:
            cl[last] += cl[i]
            cl[i] = 0
        if not used[i]:
            res += 1
        used[i] = True
    i += 1
    if i==last:
        break

if cl[last]<0:
    res = -1
print(res)
# print(cl)

# -*- coding: utf-8 -*-
d = set()
s = list(input())
n = len(s)
for c in s:
    d.add(c)

res = 10**5
for c in d:
    cnt = 0
    ss = list(s)
    nn = n
    # print(ss,nn,c)
    while True:
        if len(set(ss))==1:
            break
        cnt += 1
        for i in range(nn-1):
            if ss[i+1]==c:
                ss[i] = c
        ss.pop()
        nn -= 1
    res = min(res, cnt)
print(res)

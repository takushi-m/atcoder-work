# -*- coding: utf-8 -*-
n = int(input())
dl = [int(input()) for _ in range(n)]
dl.sort(reverse=True)

cnt = 1
d = dl[0]
for i in range(1,n):
    if d>dl[i]:
        cnt += 1
        d = dl[i]

print(cnt)
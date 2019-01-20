# -*- coding: utf-8 -*-
n = int(input())
hl = list(map(int, input().split()))

res = 0

for i in range(n):
    if hl[i]==0:
        continue

    while hl[i]>0:
        res += 1
        for j in range(i,n):
            if hl[j]==0:
                break
            hl[j] -= 1

print(res)

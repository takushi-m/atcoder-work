# -*- coding: utf-8 -*-
n = int(input())
hl = list(map(int, input().split()))

hl[0] -= 1
for i in range(1,n):
    if hl[i-1] <= hl[i]-1:
        hl[i] -= 1

    if hl[i-1]>hl[i]:
        print("No")
        exit()

print("Yes")

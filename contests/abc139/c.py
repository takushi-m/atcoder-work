# -*- coding: utf-8 -*-
n = int(input())
hl = list(map(int, input().split()))

al = [0 for _ in range(n)]
for i in range(n-1,0,-1):
    if hl[i-1]>=hl[i]:
        al[i-1] = al[i]+1

print(max(al))

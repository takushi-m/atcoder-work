# -*- coding: utf-8 -*-
n,q = map(int, input().split())
al = list(map(int, input().split()))
acc = [0 for _ in range(n+1)]
for i in range(n):
    acc[i+1] = acc[i]+al[i]
xl = [int(input()) for _ in range(q)]

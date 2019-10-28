# -*- coding: utf-8 -*-
n = int(input())
al = [int(input()) for _ in range(n)]
al2 = sorted(al)

for i in range(n):
    if al[i]==al2[-1]:
        print(al2[-2])
    else:
        print(al2[-1])
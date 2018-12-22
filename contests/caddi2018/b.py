# -*- coding: utf-8 -*-
n = int(input())
al = [int(input()) for _ in range(n)]

for a in al:
    if a%2==1:
        print("first")
        exit()
print("second")

# -*- coding: utf-8 -*-
n,k = map(int, input().split())
s = input()

rl = 0
for i in range(n-1):
    if s[i:i+2]=="RL":
        rl += 1

if k>rl:
    print(n-1)
else:
    res = n - 2*(rl-k)
    if s[0]=="L":
        res -= 1
    if s[n-1]=="R":
        res -= 1

    print(res)
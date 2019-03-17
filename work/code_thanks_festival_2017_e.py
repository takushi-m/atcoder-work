# -*- coding: utf-8 -*-
from itertools import product
memo= {}
for n in range(1,5+1):
    memo[n] = {}
    for x in product([9,11,8,10,12], repeat=n):
        m = sum([10**i * x[i] for i in range(n)])
        memo[n][m] = x

n = int(input())
res = ["0"]*n
r = n//5
if n%5!=0:
    r += 1
for i in range(r):
    q = ["0"]*n
    for j in range(5):
        if 5*i+j<n:
            q[5*i+j] = str(10**j)
    print("? "+" ".join(q), flush=True)
    ans = int(input())
    k = min(5,n-5*i)
    for j in range(k):
        if memo[k][ans][j]==9 or memo[k][ans][j]==11:
            res[5*i+j] = "1"

print("! "+" ".join(res), flush=True)

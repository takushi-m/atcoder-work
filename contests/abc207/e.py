import sys
sys.setrecursionlimit(10**6)
from functools import lru_cache

n = int(input())
al = list(map(int, input().split()))
acc = [0 for _ in range(n+1)]
for i in range(n):
    acc[i+1] = acc[i]+al[i]

mod = 10**9+7

@lru_cache(maxsize=10**6)
def f(i,k):
    c = 0
    for j in range(i+1,n+1):
        x = acc[j]-acc[i]
        if x%k==0:
            if j==n:
                c += 1
            else:
                c += f(j,k+1)
                c %= mod
    return c % mod

print(f(0,1))

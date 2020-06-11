from functools import lru_cache
import sys
sys.setrecursionlimit(10**6)

mod = 10**9 + 7
n = int(input())
s = input()
tl = [input() for _ in range(n)]

@lru_cache(maxsize=10**6)
def f(ss):
    if ss=="":
        return 1

    res = 0
    for t in tl:
        if ss.startswith(t):
            res += f(ss[len(t):])
            res %= mod
    return res

print(f(s))
from functools import lru_cache

n = int(input())

@lru_cache(maxsize=10**5)
def f(x):
    if x == 0:
        return 2
    elif x == 1:
        return 1
    else:
        return f(x-1) + f(x-2)

print(f(n))
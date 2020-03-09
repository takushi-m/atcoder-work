from functools import lru_cache

n,m = map(int, input().split())

e = [0]*n
for _ in range(m):
    x,y = map(int, input().split())
    x -= 1
    y -= 1
    e[x] |= 1<<y

@lru_cache(maxsize=1<<n)
def f(s):
    if s==0:
        return 1
    res = 0
    for i in range(n):
        if (s>>i)&1==1 and s&e[i]==0:
            res += f(s^(1<<i))
    return res

print(f((1<<n)-1))
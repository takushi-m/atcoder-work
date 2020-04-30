from collections import defaultdict
mod = 10**9 + 7
n = int(input())
d = defaultdict(int)
for c in list(input()):
    d[c] += 1

res = 1
for c in d:
    res *= (d[c]+1)
    res %= mod
res = res + mod - 1
res %= mod
print(res)
from itertools import combinations
from collections import defaultdict

n,x = map(int, input().split())
wl = [int(input()) for _ in range(n)]

d = defaultdict(int)
m = n//2
for r in range(m+1):
    for cl in combinations(range(m), r):
        w = sum([wl[i] for i in cl])
        d[w] += 1

res = 0
for r in range(n-m+1):
    for cl in combinations(range(m,n), r):
        w = sum([wl[i] for i in cl])
        if x-w in d:
            res += d[x-w]
print(res)
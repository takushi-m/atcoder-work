from collections import defaultdict

n = int(input())
al = list(map(int, input().split()))

r = defaultdict(int)
l = defaultdict(int)
for i in range(n):
    r[al[i]+i] += 1
    l[i-al[i]] += 1

res = 0
for k in r:
    res += r[k]*l[k]

print(res)
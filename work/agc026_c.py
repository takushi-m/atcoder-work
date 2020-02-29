from itertools import combinations
from collections import defaultdict
n = int(input())
s = input()

d = defaultdict(int)
left = set()
for r in range(n+1):
    for cl in combinations(range(n),r):
        sl = ""
        sr = ""
        for i in range(n):
            if i in cl:
                sl += s[i]
            else:
                sr += s[i]
        left.add(sl+","+sr)
        d[sl+","+sr] += 1

res = 0
for r in range(n+1):
    for cl in combinations(range(n,2*n),r):
        sl = ""
        sr = ""
        for i in range(n,2*n):
            if i in cl:
                sl = s[i] + sl
            else:
                sr = s[i] + sr
        if sr+","+sl in left:
            res += d[sr+","+sl]

print(res)
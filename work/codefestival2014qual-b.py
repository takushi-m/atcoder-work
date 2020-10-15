from collections import defaultdict
from string import ascii_uppercase

s1 = input()
s2 = input()
s3 = input()

c1 = defaultdict(int)
c2 = defaultdict(int)
c3 = defaultdict(int)

n = len(s1)//2
for i in range(2*n):
    c1[s1[i]] += 1
    c2[s2[i]] += 1
    c3[s3[i]] += 1

n_min = 0
n_max = 0
for c in ascii_uppercase:
    n_min += max(c3[c]-c2[c], 0)
    n_max += min(c1[c], c3[c])

if n_min <= n <= n_max:
    print("YES")
else:
    print("NO")
from itertools import product

n = int(input())
al = list(map(int, input().split()))
res = 0
for p in product([-1,0,1], repeat=n):
    bl = [al[i]+p[i] for i in range(n)]
    m = 1
    for b in bl:
        m *= b
    if m%2==0:
        res += 1
print(res)
from itertools import combinations

n,m,x = map(int, input().split())

cl = []
al = []
for _ in range(n):
    xl = list(map(int, input().split()))
    cl.append(xl[0])
    al.append(xl[1:])

res = 10**9
for r in range(n+1):
    for c in combinations(range(n), r=r):
        s = 0
        xl = [0]*m
        for i in c:
            s += cl[i]
            xl = [xl[j]+al[i][j] for j in range(m)]
        if all([q>=x for q in xl]):
            res = min(res,s)

if res==10**9:
    print(-1)
else:
    print(res)
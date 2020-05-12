n,k = map(int, input().split())
al = list(map(int, input().split()))

next = [[0]*n for _ in range(60)]
for i in range(n):
    next[0][i] = al[i]-1

for p in range(1,60):
    for i in range(n):
        next[p][i] = next[p-1][next[p-1][i]]

res = 0
for p in range(59,-1,-1):
    if (k>>p)&1 == 1:
        res = next[p][res]

print(res+1)
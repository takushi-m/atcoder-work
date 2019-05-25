n,m = map(int, input().split())
id = [0]*(n+1)

for _ in range(m):
    l,r = map(int, input().split())
    id[l-1] += 1
    id[r] -= 1

res = 0
x = 0
for i in range(n+1):
    x += id[i]
    if x==m:
        res += 1

print(res)

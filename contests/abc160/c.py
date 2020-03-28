k,n = map(int, input().split())
al = list(map(int, input().split()))

res = al[-1] - al[0]
for i in range(1,n):
    r = k - al[i] + al[i-1]
    res = min(res, r)

print(res)
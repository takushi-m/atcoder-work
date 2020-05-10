a,b,c,k = map(int, input().split())

res = min(a,k)
k -= a

if k>0:
    k -= b

if k>0:
    res -= min(c,k)

print(res)
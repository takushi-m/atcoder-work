a,b,m = map(int, input().split())
al = list(map(int, input().split()))
bl = list(map(int, input().split()))
xyc = [list(map(int, input().split())) for _ in range(m)]

da = {}
for i in range(a):
    da[i+1] = al[i]
db = {}
for i in range(b):
    db[i+1] = bl[i]

res = min(al)+min(bl)
for x,y,c in xyc:
    res = min(res, da[x]+db[y]-c)

print(res)

n = int(input())

g = []
if n%2==1:
    g.append([n])
    for i in range(1,n//2+1):
        g.append([i,n-i])
else:
    for i in range(1,n//2+1):
        g.append([i,n-i+1])

res = set()
for i in range(len(g)):
    for j in range(len(g)):
        if i==j:
            continue
        for v in g[i]:
            for u in g[j]:
                res.add((min(v,u),max(v,u)))
print(len(res))
for v,u in res:
    print(v,u)
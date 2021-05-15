n = int(input())
g = [[] for _ in range(n)]
for _ in range(n-1):
    u,v,w = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append((v,w))
    g[v].append((u,w))


d = [-10**9]*n
d[0] = 0
q = [0]
while len(q)>0:
    v = q.pop()
    for u,w in g[v]:
        if d[u]>=0:
            continue
        d[u] = d[v]^w
        q.append(u)

mod = 10**9+7
res = 0
for k in range(60):
    p = 0
    for i in range(n):
        if (d[i]>>k)&1 == 1:
            p += 1
    res += p*(n-p)*pow(2,k,mod)
    res %= mod
print(res)
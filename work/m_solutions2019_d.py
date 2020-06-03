n = int(input())
ab = [list(map(int, input().split())) for _ in range(n-1)]
cl = list(map(int, input().split()))
cl.sort(reverse=True)

e = [set() for _ in range(n)]
for a,b in ab:
    a -= 1
    b -= 1
    e[a].add(b)
    e[b].add(a)

used = [False]*n
q = [0]

res = [0]*n
i = 0
while len(q)>0:
    u = q.pop()
    res[u] = cl[i]
    used[u] = True
    i += 1
    for v in e[u]:
        if not used[v]:
            q.append(v)

r = 0
for a,b in ab:
    r += min(res[a-1], res[b-1])
print(r)
print(*res)
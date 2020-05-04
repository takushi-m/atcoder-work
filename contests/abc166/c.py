n,m = map(int, input().split())
hl = list(map(int, input().split()))

e = [[] for _ in range(n)]
for _ in range(m):
    u,v = map(int, input().split())
    u -= 1
    v -= 1
    e[u].append(v)
    e[v].append(u)

res = 0
for u in range(n):
    flag = True
    h = hl[u]
    for v in e[u]:
        if hl[v]>=h:
            flag = False
            break
    # print(u,flag)
    if flag:
        res += 1
print(res)
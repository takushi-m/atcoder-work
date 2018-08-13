line = input().split(" ")
N = int(line[0])
M = int(line[1])

g = {}
E = []
for _ in range(M):
    line = input().split(" ")
    a = line[0]
    b = line[1]
    E.append((a,b))
    if not a in g:
        g[a] = []
    g[a].append(b)

    if not b in g:
        g[b] = []
    g[b].append(a)

def judge(a, b):
    flags = {}
    for v in g:
        flags[v] = False
    q = [a]
    flags[a] = True
    while len(q)>0:
        v = q.pop(0)
        for u in g[v]:
            if (v==a and u==b) or (v==b and u==a):
                continue
            elif not flags[u]:
                flags[u] = True
                q.append(u)
    ret = True
    for v in flags:
        ret = ret and flags[v]

    return not ret

cnt = 0
for e in E:
    if judge(e[0],e[1]):
        cnt += 1

print(cnt)

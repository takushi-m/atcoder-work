n,m = map(int, input().split())
e = [set() for _ in range(n)]
for _ in range(m):
    u,v = map(int, input().split())
    u -= 1
    v -= 1
    e[u].add(v)
    e[v].add(u)

def dfs():
    col = [-1]*n
    col[0] = 0
    q = [0]
    while len(q)>0:
        v = q.pop()
        c = col[v]
        for u in e[v]:
            if col[u]<0:
                col[u] = (c+1)%2
                q.append(u)
            else:
                if c==col[u]:
                    return False
    return True

if not dfs():
    print(n*(n-1)//2 - m)
    exit()

visited = [False]*n
visited[0] = True
num = [0,0]
q = [(0,0)]
while len(q)>0:
    u,d = q.pop()
    num[d%2] += 1
    for v in e[u]:
        if visited[v]:
            continue
        q.append((v,d+1))
        visited[v] = True

print(num[0]*num[1]-m)
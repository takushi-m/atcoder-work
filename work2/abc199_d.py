n,m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    a,b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)


visited = [False]*n
def visit(start, elm):
    visited[start] = True
    elm.append(start)
    q = [start]
    while len(q)>0:
        v = q.pop()
        for u in g[v]:
            if not visited[u]:
                visited[u] = True
                elm.append(u)
                q.append(u)

def count(p, colors, elm):
    v = elm[p]
    for u in g[v]:
        if colors[v]==colors[u]:
            return 0
    if len(elm)==p+1:
        return 1
    
    res = 0
    for c in [1,2,3]:
        colors[elm[p+1]] = c
        res += count(p+1, colors, elm)
    colors[elm[p+1]] = 0
    return res

res = 1
for v in range(n):
    if visited[v]:
        continue

    colors = [0]*n
    elm = []
    visit(v,elm)
    colors[v] = 1
    cnt = count(0, colors, elm)
    res *= 3*cnt

print(res)
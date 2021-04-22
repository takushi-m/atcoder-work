from collections import deque
MAX=10**9
n = int(input())

g = [[] for _ in range(n)]
for _ in range(n-1):
    a,b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

def bfs(s):
    cost = [MAX]*n
    cost[s] = 0
    q = deque([s])
    while len(q)>0:
        v = q.popleft()
        for u in g[v]:
            if cost[u]>cost[v]+1:
                cost[u] = cost[v]+1
                q.append(u)
    
    v = s
    for i in range(n):
        if MAX>cost[i]>cost[v]:
            v = i
    return (v, cost[v])


v, _ = bfs(0)
_,res = bfs(v)
print(res+1)

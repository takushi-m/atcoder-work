import heapq

n = int(input())
e = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int, input().split())
    e[a].append(b)
    e[b].append(a)

used = [False]*(n+1)
res = []
q = [1]
while len(q)>0:
    a = heapq.heappop(q)
    res.append(a)
    used[a] = True
    for b in e[a]:
        if not used[b]:
            heapq.heappush(q,b)

print(*res)
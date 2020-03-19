import heapq


n = int(input())
e = [[] for _ in range(n)]
for _ in range(n-1):
    a,b = map(int, input().split())
    a -= 1
    b -= 1
    e[a].append(b)
    e[b].append(a)

res = []
used = set()
q = [0]
heapq.heapify(q)
while len(q)>0:
    x = heapq.heappop(q)
    res.append(x)
    used.add(x)
    for y in e[x]:
        if y not in used:
            heapq.heappush(q, y)

print(*[x+1 for x in res])

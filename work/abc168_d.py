n,m = map(int, input().split())
e = [set() for _ in range(n)]
for _ in range(m):
    a,b = map(int, input().split())
    a -= 1
    b -= 1
    e[a].add(b)
    e[b].add(a)

p = [-1]*n
p[0] = 0
q = [0]
while len(q)>0:
    u = q.pop(0)
    for v in e[u]:
        if p[v]==-1:
            p[v] = u
            q.append(v)
if min(p)==-1:
    print("No")
else:
    print("Yes")
    for i in range(1,n):
        print(p[i]+1)
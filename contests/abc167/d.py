n,k = map(int, input().split())
al = [0]+list(map(int, input().split()))

s = 1
visited = [0]*(n+1)
cnt = 0
for i in range(k):
    s = al[s]
    cnt += 1
    if visited[s]>0:
        r = k - cnt
        l = cnt - visited[s]
        for _ in range(r%l):
            s = al[s]
        break
    else:
        visited[s] = cnt
print(s)
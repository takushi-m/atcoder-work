n = int(input())
xyz = [list(map(int, input().split())) for _ in range(n)]

def calc(a,b,c,p,q,r):
    return abs(p-a) + abs(q-b) + max(0,r-c)

dist = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        a,b,c = xyz[i]
        p,q,r = xyz[j]
        dist[i][j] = calc(a,b,c,p,q,r)

dp = [[-1]*n for _ in range(1<<n)]

def dfs(s,v):
    if dp[s][v] >= 0:
        return dp[s][v]
    
    if s == (1<<n)-1 and v==0:
        dp[s][v] = 0
        return 0
    
    ans = 10**18
    for u in range(n):
        if not (s>>u & 1):
            ans = min(ans, dfs(s | 1<<u, u) + dist[v][u])
        
    dp[s][v] = ans
    return ans

print(dfs(0,0))
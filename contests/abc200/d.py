from collections import deque
n = int(input())
al = list(map(int, input().split()))

for i in range(n):
    al[i] %= 200

dp = [[0]*210 for _ in range(210)]
dp[0][0] = 1
for i in range(n):
    for j in range(200):
        dp[i+1][j] += dp[i][j]
        dp[i+1][j] %= 200

        x = (j+al[i])%200
        dp[i+1][x] += dp[i][j]
        dp[i+1][x] %= 200

# print(dp[n])

p = 1000
idx = -1
for i in range(200):
    if dp[n][i]>1:
        p = min(p, dp[n-1][i])
        idx = i

if p==1000:
    print("No")
    exit()

res = []
def rec(i,j,keiro,ans):
    if len(res)>2:
        return
    if i==0:
        if j==0:
            res.append(list(keiro))
            ans.append(keiro)
        return

    if dp[i-1][j]>0:
        rec(i-1,j,keiro,ans)
    
    x = (j+200-al[i-1])%200
    if dp[i-1][x]>0:
        keiro.appendleft(i) # 1-indexで表示したい
        rec(i-1,x,keiro,ans)
        keiro.popleft()

rec(n,idx,deque([]), [])
print("Yes")
print(len(res[0]), *res[0])
print(len(res[1]), *res[1])

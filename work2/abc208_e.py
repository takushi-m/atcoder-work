from collections import defaultdict

n,k = input().split()
k = int(k)
inf = k+1
nl = [int(n[i]) for i in range(len(n))]

dp = defaultdict(int)
for i in range(len(nl)):
    nxt = defaultdict(int)

    if i==0:
        for x in range(1,nl[i]+1):
            nxt[(x,x<nl[i])] = 1
    else:
        for (prod,less),cnt in dp.items():
            if less:
                for x in range(10):
                    next_prod = min(inf, prod*x)
                    nxt[(next_prod,True)] += cnt
            else:
                for x in range(nl[i]+1):
                    next_prod = min(inf,prod*x)
                    nxt[(next_prod,x<nl[i])] += cnt

        for x in range(1,10):
            nxt[(x,True)] += 1
    dp = nxt
    # print(dp)

cnt = 0
for p in dp:
    if p[0]<=k:
        cnt += dp[p]
print(cnt)
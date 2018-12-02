# -*- coding: utf-8 -*-
n = int(input())
l = []

for i in range(1,11):
    x = 6**i
    l.append(x)
for i in range(1,11):
    x = 9**i
    l.append(x)

# l.sort()
dp = [i for i in range(n+1)]
for x in l:
    if x>n:
        continue
    for i in range(n-x+1):
        dp[i+x] = min(dp[i+x], dp[i]+1)
print(dp[n])

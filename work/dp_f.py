# -*- coding: utf-8 -*-
s = input()
ns = len(s)
t = input()
nt = len(t)

dp = [[0 for _ in range(ns+1)] for _ in range(nt+1)]

for ti in range(nt):
    for si in range(ns):
        if t[ti]==s[si]:
            add = 1
        else:
            add = 0

        dp[ti+1][si+1] = max(
            dp[ti][si]+add,
            dp[ti+1][si],
            dp[ti][si+1]
        )

# print(dp[nt][ns])

res = []
ti = nt
si = ns
while ti>0 and si>0:
    if t[ti-1]==s[si-1]:
        res.append(s[si-1])
        si -= 1
        ti -= 1
    elif dp[ti][si-1]>dp[ti-1][si]:
        si -= 1
    else:
        ti -= 1

res.reverse()
print("".join(res))

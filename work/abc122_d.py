# -*- coding: utf-8 -*-
n = int(input())
MOD = 10**9 + 7

# agc, acg, gac, agxc, axgc
def ok(last4):
    if last4.count("AGC")>0:
        return False
    if last4.count("ACG")>0:
        return False
    if last4.count("GAC")>0:
        return False
    if last4[:2]=="AG" and last4[3]=="C":
        return False
    if last4[0]=="A" and last4[2:]=="GC":
        return False
    return True

memo = [{} for _ in range(n+1)]
def dfs(cur, last3):
    if last3 in memo[cur]:
        return memo[cur][last3]
    if cur==n:
        return 1

    res = 0
    for c in "AGCT":
        if ok(last3+c):
            res = (res + dfs(cur+1, last3[1:]+c))%MOD
    memo[cur][last3] = res
    return res

print(dfs(0, "TTT"))

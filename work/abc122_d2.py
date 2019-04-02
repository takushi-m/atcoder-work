# -*- coding: utf-8 -*-
import re
n = int(input())
MOD = 10**9 + 7

def dfs(cur, s):
    if cur==n:
        if re.search(r"(AGC|ACG|GAC|AG.C|A.GC)", s):
            return 0
        else:
            return 1
    res = 0
    for c in "AGCT":
        res = (res + dfs(cur+1, s+c))%MOD

    return res

print(dfs(0,""))

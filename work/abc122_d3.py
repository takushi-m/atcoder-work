# -*- coding: utf-8 -*-
import re
n = int(input())
MOD = 10**9 + 7

def dfs(cur, s):
    if cur==n:
            return 1
    res = 0
    for c in "AGCT":
        if not re.search(r"(AGC|ACG|GAC|AG.C|A.GC)", s+c):
            res = (res + dfs(cur+1, s[1:]+c))%MOD

    return res

print(dfs(0,"TTT"))

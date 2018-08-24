# -*- coding: utf-8 -*-
line = input().split()
n = int(line[0])
m = int(line[1])

path = [[] for _ in range(n)]
for _ in range(m):
    line = input().split()
    a = int(line[0])-1
    b = int(line[1])-1
    path[a].append(b)

def dfs(i, s):
    if i==n-1:
        if s==2:
            return True
        else:
            return False

    for e in path[i]:
        if dfs(e, s+1):
            return True
    return False

if dfs(0,0):
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")

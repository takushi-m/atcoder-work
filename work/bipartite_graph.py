# coding=utf-8

n = 4
E = [
    [0,1]
    ,[0,3]
    ,[1,2]
    ,[2,3]
]

g = [[] for _ in range(n)]
for e in E:
    g[e[0]].append(e[1])

color = [0 for _ in range(n)]

def dfs(v, c):
    color[v] = c
    for i in g[v]:
        if color[i]==c:
            return False
        elif color[i]==0 and not dfs(i, -1*c):
            return False
    return True

for i in range(n):
    if color[i]==0:
        if not dfs(i, 1):
            print("No")
            exit()
print("Yes")

# coding=utf-8

N = int(input())
tree = [[]for x in range(N)]
depth = [0 for x in range(N)]
for _ in range(N-1):
    line = input().split(" ")
    a = int(line[0])-1
    b = int(line[1])-1
    c = int(line[2])
    tree[a].append((b, c))
    tree[b].append((a, c))

line = input().split(" ")
Q = int(line[0])
K = int(line[1])-1

# def dfs(v, p, d):
#     depth[v] = d
#     for e in tree[v]:
#         if e[0]==p:
#             continue
#         dfs(e[0], v, d+e[1])
# dfs(K, -1, 0)

s = [(K, -1, 0)]
while len(s)>0:
    (v, p, d) = s.pop()
    depth[v] = d
    for e in tree[v]:
        if e[0]==p:
            continue
        s.append((e[0], v, d+e[1]))


for _ in range(Q):
    line = input(" ").split(" ")
    x = int(line[0])-1
    y = int(line[1])-1
    print(str(depth[x]+depth[y]))

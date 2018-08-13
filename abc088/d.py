# coding=utf-8

line = input().split(" ")
H = int(line[0])
W = int(line[1])

s = []
cnt_w = 0
for _ in range(H):
    line = list(input())
    for x in line:
        if x==".":
            cnt_w += 1
    s.append(line)

INF = 100000

diff = [
    [0,1]
    ,[0,-1]
    ,[1,0]
    ,[-1,0]
]

def dfs():
    q = []
    m = []
    for i in range(H):
        m.append([INF for _ in range(W)])
    q.append((0,0))
    m[0][0] = 1

    while len(q)>0:
        p = q.pop(0)
        if H-1==p[0] and W-1==p[1]:
            break

        for d in diff:
            ni = p[0]+d[0]
            nj = p[1]+d[1]
            if 0<=ni<H and 0<=nj<W:
                if s[ni][nj]=="." and m[ni][nj]==INF:
                    q.append((ni,nj))
                    m[ni][nj] = m[p[0]][p[1]]+1

    return m[H-1][W-1]

r = dfs()

if r == INF:
    print("-1")
else:
    print(cnt_w - r)

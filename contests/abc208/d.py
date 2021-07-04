# def warshallFloyd(d,n):
#     for k in range(n):
#         for i in range(n):
#             for j in range(n):
#                 d[i][j] = min(d[i][j], d[i][k]+d[k][j])
#     return d

inf = 10**10
n,m = map(int, input().split())
d = [[inf]*n for _ in range(n)]
for _ in range(m):
    a,b,c = map(int, input().split())
    d[a-1][b-1] = c

res = 0
for k in range(n):
    for i in range(n):
        for j in range(n):
            d[i][j] = min(d[i][j], d[i][k]+d[k][j])
    for i in range(n):
        for j in range(n):
            if i==j:
                continue
            if d[i][j]==inf:
                continue
            res += d[i][j]

print(res)
            
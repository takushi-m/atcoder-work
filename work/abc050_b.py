n = int(input())
tl = list(map(int, input().split()))
m = int(input())
px = [list(map(int, input().split())) for _ in range(m)]

s = sum(tl)
for i in range(m):
    p,x = px[i]
    print(s-tl[p-1]+x)
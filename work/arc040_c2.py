n = int(input())
sl = [list(input()) for _ in range(n)]

cnt = 0
for r in range(n):
    c = -1
    for x in range(n):
        if sl[r][x]==".":
            c = x

    if c<0:
        continue
    cnt += 1
    if r==n-1:
        continue
    for x in range(c,n):
        sl[r+1][x] = "o"

print(cnt)
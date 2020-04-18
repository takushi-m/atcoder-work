n,m = map(int, input().split())

d = [0]*m
for _ in range(n):
    flag = True
    for a in map(int, input().split()):
        if flag:
            flag = False
            continue
        d[a-1] += 1

cnt = 0
for i in range(m):
    if d[i]==n:
        cnt += 1
print(cnt)
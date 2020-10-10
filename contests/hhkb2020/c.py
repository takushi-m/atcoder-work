n = int(input())
pl = list(map(int, input().split()))

m = 200000+10
used = [0]*m
idx = 0

for p in pl:
    used[p] = 1
    if idx==p:
        while idx<=m and used[idx]==1:
            idx += 1
    print(idx)

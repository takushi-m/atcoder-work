n = int(input())
al = [int(input())-1 for _ in range(n)]
used = [False]*n
s = 0
res = 0
used[s] = True
while s!=1:
    s = al[s]
    if used[s]:
        print(-1)
        exit()
    used[s] = True
    res += 1
print(res)
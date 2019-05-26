n,m = map(int, input().split())

kl = []
sl = []
for _ in range(m):
    line = list(map(int, input().split()))
    k = line[0]
    s = line[1:]
    kl.append(k)
    sl.append(s)
p = list(map(int, input().split()))

res = 0

for i in range(2**n):
    s = []
    for j in range(n):
        if i>>j&1==1:
            s.append(j+1)
    flag = True
    for mi in range(m):
        cnt = 0
        for si in s:
            if si in sl[mi]:
                cnt += 1
        if cnt%2!=p[mi]:
            flag = False
        if not flag:
            break
    if flag:
        res += 1

print(res)

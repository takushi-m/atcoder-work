n = int(input())
al = list(map(int, input().split()))
bl = [0]*(n+1)
acc = [0]*(n+2)
for i in range(n+1):
    acc[i+1] = al[i]+acc[i]

res = 0
for d in range(n+1):
    if d==0:
        res += 1
        bl[0] = 1 - al[0]
    else:
        r1 = 2*bl[d-1] - al[d]
        r2 = acc[-1] - acc[d+1]
        bl[d] = min(r1,r2)
        res += al[d]+bl[d]
    if bl[d]<0:
        print(-1)
        exit()

print(res)
n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]

res = 0
for i in range(n):
    for j in range(i+1,n):
        t1,l1,r1 = l[i]
        t2,l2,r2 = l[j]

        if r1<l2:
            continue
        if r1==l2:
            if t1 in (2,4) or t2 in (3,4):
                continue
        if r2<l1:
            continue
        if r2==l1:
            if t1 in (3,4) or t2 in (2,4):
                continue

        res += 1

print(res)



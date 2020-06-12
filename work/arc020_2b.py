n,c = map(int, input().split())
al = [int(input()) for _ in range(n)]

res = 10**9
for a1 in range(1,11):
    for a2 in range(1,11):
        if a1==a2:
            continue
        cost = 0
        for i in range(n):
            a = al[i]
            if i%2==0 and a!=a1:
                cost += c
            elif i%2==1 and a!=a2:
                cost += c
        res = min(res, cost)

print(res)
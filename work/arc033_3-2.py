q = int(input())
tx = [list(map(int, input().split())) for _ in range(q)]

m = 500
n = 200010//m
l1 = [0]*(n+10)
l2 = [set() for _ in range(n+10)]

for t,x in tx:
    if t==1:
        l2[x//m].add(x)
        l1[x//m] += 1
        continue

    i = 0
    while l1[i]<x:
        x -= l1[i]
        i += 1
    l = sorted(list(l2[i]))
    print(l[x-1])
    l2[i].remove(l[x-1])
    l1[i] -= 1
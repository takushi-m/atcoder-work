from itertools import combinations

n = int(input())
al = list(map(int, input().split()))

d = {}
for c in range(1,9):
    for r in combinations(range(1,1+min(n,8)), c):
        p = sum(al[x-1] for x in r) % 200

        if p in d:
            print("Yes")
            print(len(r), *r)
            print(len(d[p]), *d[p])
            exit()
        else:
            d[p] = r

print("No")
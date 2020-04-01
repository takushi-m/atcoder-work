from itertools import combinations

n,c = map(int, input().split())
al = [int(input())-1 for _ in range(n)]

res = 10**10
for comb in combinations(range(10),2):
    r = 0
    for i in range(n):
        if al[i]!=comb[i%2]:
            r += c
    res = min(res,r)

    r = 0
    for i in range(n):
        if al[i]!=comb[(i+1)%2]:
            r += c
    res = min(res,r)

print(res)
from itertools import permutations

l = [int(input()) for _ in range(5)]
res = 10**9
for r in permutations(l, r=5):
    x = 0
    for i in range(4):
        x += r[i]
        if r[i]%10>0:
            x += 10-r[i]%10
    x += r[-1]

    res = min(res, x)
print(res)
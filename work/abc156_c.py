n = int(input())
xl = list(map(int, input().split()))

res = 10**9
for p in range(1,101):
    s = 0
    for x in xl:
        s += (x-p)**2
    res = min(res,s)

print(res)
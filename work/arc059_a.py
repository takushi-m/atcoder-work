n = int(input())
al = list(map(int, input().split()))

res = 10**9
for x in range(-100,101):
    res = min(res, sum([(x-a)**2 for a in al]))

print(res)
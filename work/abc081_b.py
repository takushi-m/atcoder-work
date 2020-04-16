n = int(input())
al = list(map(int, input().split()))

res = 10**9
for a in al:
    c = 0
    while a%2==0:
        a //= 2
        c += 1
    res = min(res, c)
print(res)
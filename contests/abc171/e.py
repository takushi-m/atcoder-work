n = int(input())
al = list(map(int, input().split()))

x = 0
for a in al:
    x ^= a

res = []
for a in al:
    res.append(x^a)

print(*res)
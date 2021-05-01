n,D,H = map(int, input().split())

res = 0
for _ in range(n):
    d,h = map(int, input().split())
    a = (H-h)/(D-d)
    # h = a*d + b
    b = h - a*d
    res = max(res, b)
print(res)
k, s = map(int, input().split())

res = 0
for x in range(k+1):
    for y in range(k+1):
        z = s - x - y
        if 0<=z<=k:
            res += 1
print(res)
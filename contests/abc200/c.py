n = int(input())
al = list(map(int, input().split()))

d = {x: 0 for x in range(200)}
for i in range(n):
    p = al[i] % 200
    d[p] += 1


res = 0
for k in d:
    if d[k] > 1:
        res += d[k] * (d[k]-1)
print(res // 2)

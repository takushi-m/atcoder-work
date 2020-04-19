n,m = map(int, input().split())

d = [0]*n
for _ in range(m):
    a,b = map(int, input().split())
    a -= 1
    b -= 1
    d[a] += 1
    d[b] += 1

for x in d:
    print(x)
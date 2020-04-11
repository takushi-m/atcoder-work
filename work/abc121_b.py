n,m,c = map(int, input().split())
bl = list(map(int, input().split()))

res = 0
for _ in range(n):
    al = list(map(int, input().split()))
    s = c + sum([al[i]*bl[i] for i in range(m)])
    if s>0:
        res += 1
print(res)
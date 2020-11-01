n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]

res = 0
for a,b in ab:
    res += b*(b+1)//2 - a*(a+1)//2 + a
print(res)
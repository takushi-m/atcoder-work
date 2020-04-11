n = int(input())
k = int(input())
xl = list(map(int, input().split()))

res = 0
for i in range(n):
    res += min(xl[i]*2, (k-xl[i])*2)
print(res)
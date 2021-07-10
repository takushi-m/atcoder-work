n = int(input())
cl = list(map(int, input().split()))
cl.sort()
mod = 10**9+7

res = 1
for i in range(n):
    res *= cl[i] - i
    res %= mod
print(res)
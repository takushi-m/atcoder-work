n,k = map(int, input().split())
al = list(map(int, input().split()))

acc = [0]*(n+1)
for i in range(n):
    acc[i+1] = acc[i]+al[i]

res = 0
for i in range(n-k+1):
    res += acc[i+k]-acc[i]

print(res)
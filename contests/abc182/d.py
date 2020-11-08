n = int(input())
al = list(map(int, input().split()))

acc = [0]*(n+1)
for i in range(n):
    acc[i+1] = acc[i]+al[i]

acc2 = [0]*(n+1)
m = -10**15
for i in range(n+1):
    if acc[i]>m:
        m = acc[i]
    acc2[i] = m

res = 0
p = 0
for i in range(n):
    res = max(res, p+acc2[i+1])
    p = p + acc[i+1]

print(res)
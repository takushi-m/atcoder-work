k,q = map(int, input().split())
dl = list(map(int, input().split()))
nxm = [list(map(int, input().split())) for _ in range(q)]

D = sum(dl)
acc = [0]*(k+1)
for i in range(k):
    acc[i+1] += acc[i] + dl[i]
print(acc)

res = 0
for n,x,m in nxm:
    res += n - (x+D*(n//k)+acc[n%k])//m

print(res)
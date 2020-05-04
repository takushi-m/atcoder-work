from collections import Counter
mod = 998244353

n = int(input())
dl = list(map(int, input().split()))
c = Counter(dl)

if dl[0]!=0:
    print(0)
    exit()

if c[0]!=1:
    print(0)
    exit()

res = 1
for x in range(max(dl)):
    res *= pow(c[x],c[x+1],mod)
    res %= mod

print(res)
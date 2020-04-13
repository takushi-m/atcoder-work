n,k = map(int, input().split())
mod = 10**9 + 7

al = [0]*(k+1)
for x in range(1,k+1):
    al[x] = pow(k//x,n,mod)

for x in range(k,0,-1):
    for b in range(2, k//x+1):
        al[x] -= al[x*b]

res = 0
for i in range(k+1):
    res += i*al[i]
    res %= mod
print(res)
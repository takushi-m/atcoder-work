def modpow(a,n,m):
    res = 1
    while n>0:
        if n%2==1:
            res = (res * a) % m
        a = (a*a) % m
        n = n//2
    return res


def comb(n,k,mod):
    MAX = k+1
    fac = [0]*MAX
    finv = [0]*MAX
    inv = [0]*MAX

    fac[0] = 1
    fac[1] = 1
    finv[0] = 1
    finv[1] = 1
    inv[1] = 1
    for i in range(2,MAX):
        fac[i] = (fac[i-1]*i)%mod
        inv[i] = mod - (inv[mod%i] * (mod//i))%mod
        finv[i] = (finv[i-1] * inv[i])%mod

    res = 1
    for i in range(n,n-k,-1):
        res *= i
        res %= mod
    res *= finv[k]
    return res%mod

MOD = 10**9 + 7
n,a,b = map(int, input().split())

res = modpow(2,n,MOD)
res = MOD + res - comb(n,a,MOD)
res = MOD + res - comb(n,b,MOD)
res = MOD + res - 1

print(res%MOD)
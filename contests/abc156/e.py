import sys
sys.setrecursionlimit(10**6)

class BiCoeff(object):
    def __init__(self, MAX, m):
        super(BiCoeff, self).__init__()
        fac = [0]*MAX
        finv = [0]*MAX
        inv = [0]*MAX

        fac[0] = 1
        fac[1] = 1
        finv[0] = 1
        finv[1] = 1
        inv[1] = 1
        for i in range(2,MAX):
            fac[i] = (fac[i-1]*i)%m
            inv[i] = m - (inv[m%i] * (m//i))%m
            finv[i] = (finv[i-1] * inv[i])%m

        self.MAX = MAX
        self.m = m
        self.fac = fac
        self.finv = finv
        self.inv = inv

    def calc(self,n,k):
        if n<k:
            return 0
        if n<0 or k<0:
            return 0
        return (self.fac[n] * (self.finv[k]*self.finv[n-k])%self.m)%self.m


MOD = 10**9+7
n,k = map(int, input().split())

fact = [0]*(n+1)
fact[1] = 1
for i in range(2,n+1):
    fact[i] = fact[i-1]*i
    fact[i] %= MOD
bicoeff = BiCoeff(2*n+1,MOD)

res = 0
for i in range(1,n+1):
    if n-i<=k:
        res += bicoeff.calc(n-1,i-1)*bicoeff.calc(n,i)
        res %= MOD
print(res)

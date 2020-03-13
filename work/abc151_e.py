
# mod mでの二項係数を求める
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

mod = 10**9 + 7
n,k = map(int, input().split())
al = list(map(int, input().split()))
bicoeff = BiCoeff(n+k+10, mod)

al.sort()

r1 = 0
for i in range(k,n+1):
    r1 += al[i-1]*bicoeff.calc(i-1,k-1)
    r1 %= mod
r2 = 0
for i in range(0,n-k+1):
    r2 += al[i]*bicoeff.calc(n-i-1,k-1)
    r2 %= mod

print((r1+mod-r2)%mod)
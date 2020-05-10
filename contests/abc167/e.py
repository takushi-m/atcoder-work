mod = 998244353

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

n,m,k = map(int, input().split())

bicoeff = BiCoeff(10**6, mod)

res = 0
for ki in range(k+1):
    r = bicoeff.calc(n-1, ki)
    if ki==0:
        r = 1
    x = n - ki
    # print(ki, r, x, m * pow(m-1, x-1, mod))
    res += r * m * pow(m-1, x-1, mod)
    res %= mod
print(res)
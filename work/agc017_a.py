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

n,p = map(int, input().split())
al = list(map(int, input().split()))
bicoeff = BiCoeff(10**5,10**9+7)

odd = 0
even = 0
for a in al:
    if a%2==0:
        even += 1
    else:
        odd += 1

r1 = 2**even
r2 = 0
for k in range(odd+1):
    if k%2==p:
        r2 += bicoeff.calc(odd, k)
print(r1*r2)


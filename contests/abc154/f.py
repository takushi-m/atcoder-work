# -*- coding: utf-8 -*-
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

MOD = 10**9 + 7
r1,c1,r2,c2 = map(int, input().split())
bicoeff = BiCoeff(r2+c2+1, MOD)

def f(r,c):
    res = 0
    for ri in range(r+1):
        res += bicoeff.calc(c+ri,ri)
        res %= MOD
    for ci in range(c):
        res += bicoeff.calc(r+ci,r)
        res %= MOD
    return res

res = MOD + f(r2,c2) - f(r1-1,c1-1)
res %= MOD
print(res)

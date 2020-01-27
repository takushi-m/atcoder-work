# -*- coding: utf-8 -*-
from collections import defaultdict

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

MOD = 10**9+7
n, m = map(int, input().split())

pl = defaultdict(int)
x = m
p = 2
while p*p<x+10:
    while x%p==0:
        pl[p] += 1
        x //= p
    p += 1
if x>1:
    pl[x] += 1


coeff = BiCoeff(10**6, MOD)
res = 1
for k in pl:
    res *= coeff.calc(n+pl[k]-1, pl[k])
    res %= MOD
print(res)

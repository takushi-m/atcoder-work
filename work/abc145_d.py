# -*- coding: utf-8 -*-

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



x,y = map(int, input().split())

# m = (2x-y)/3
# n = (2y-x)/3

if (2*x-y)%3!=0 or (2*y-x)%3!=0:
    print(0)
    exit()

m = (2*x-y)//3
n = (2*y-x)//3

if n<0 or m<0:
    print(0)
    exit()

MOD = 10**9 + 7
coeff = BiCoeff(10**6+10, MOD)

print(coeff.calc(n+m,n))

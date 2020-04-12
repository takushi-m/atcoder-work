# a^n % m を高速に計算する
def modpow(a,n,m):
    res = 1
    while n>0:
        if n%2==1:
            res = (res * a) % m
        a = (a*a) % m
        n = n//2
    return res

mod = 10**9+7
n,k = map(int, input().split())

res = 0
for i in range(1,k+1):
    c = k//i
    c2 = 1
    while 2**c2<=c:
        c2 += 1
    c2 -= 1
    res += i*(modpow(c,n,mod)+mod-modpow(c2,n,mod))
    res %= mod
print(res)
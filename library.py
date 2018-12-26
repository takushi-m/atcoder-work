# あまり系

# aのmod Mでの逆元
def modinv(a, m):
    b = m
    u = 1
    v = 0
    while b:
        t = a//b
        a -= t*b
        a,b = b,a
        u -= t*v
        u,v = v,u
    u %= m
    if u<0:
        u += m
    return u


# a^n % m を高速に計算する
def modpow(a,n,m):
    res = 1
    while n>0:
        if n%2==1:
            res = (res * a) % m
        a = (a*a) % m
        n = n//2
    return res


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


class UnionFind():
    def __init__(self, n):
        self.par = [i for i in range(n)]

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x==y:
            return

        if x<y:
            self.par[y] = x
        else:
            self.par[x] = y

    def same(self, x, y):
        return self.find(x) == self.find(y)


"""
尺取り法

しゃくとり法は

- 「条件」を満たす区間 (連続する部分列) のうち、最小の長さを求める
- 「条件」を満たす区間 (連続する部分列) のうち、最大の長さを求める
- 「条件」を満たす区間 (連続する部分列) を数え上げる

といったことを効率良く実現できる。「条件を満たす区間」が以下のいずれかの構造になっている場合には
しゃくとり法を適用することができる。

- 区間 [left, right) が「条件」を満たすなら、それに含まれる区間も「条件」を満たす
- 区間 [left, right) が「条件」を満たすなら、それを含む区間も「条件」を満たす

テンプレート
int right = 0;
for (int left = 0; left < n; ++left) {
    while (right < n && (right を 1 個進めたときに条件を満たす)) {
        /* 実際に right を 1 進める */
        // ex: sum += a[right];
        ++right;
    }

    /* break した状態で right は条件を満たす最大なので、何かする */
    // ex: res += (right - left);

    /* left をインクリメントする準備 */
    // ex: if (right == left) ++right;
    // ex: else sum -= a[left];
}
"""


# GCD
def gcd(a,b):
    while b!=0:
        a,b = b,a%b
    return a

# ax + by = cの整数解を求める
# cはgcd(a,b)の倍数である必要あり
# x,y = extGcd(a,b)で「ax+by=gcd(a,b)」が求まるのでc//gcd(a,b)倍する
def extGcd(a,b):
    if b==0:
        return 1, 0
    y,x = extGcd(b, a%b)
    y -= a//b * x
    return x,y

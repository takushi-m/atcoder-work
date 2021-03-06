from itertools import permutations,combinations,product
from collections import deque, defaultdict
from copy import deepcopy
from operator import itemgetter
from functools import lru_cache
import heapq
import sys
sys.setrecursionlimit(2000)
from string import ascii_lowercase
from collections import Counter
from fractions import Fraction

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
        self.n = n
        self.par = [-1 for _ in range(n)]

    def same(self, x, y):
        return self.root(x)==self.root(y)

    def root(self, x):
        if self.par[x]<0:
            return x
        self.par[x] = self.root(self.par[x])
        return self.par[x]

    def unite(self,x,y):
        x = self.root(x)
        y = self.root(y)
        if x==y:
            return

        if self.par[x]>self.par[y]:
            x,y = y,x

        self.par[x] += self.par[y]
        self.par[y] = x

    def size(self,x):
        return -self.par[self.root(x)]

class WeightedUnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)
        # 根への距離を管理
        self.weight = [0] * (n+1)

    # 検索
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            y = self.find(self.par[x])
            # 親への重みを追加しながら根まで走査
            self.weight[x] += self.weight[self.par[x]]
            self.par[x] = y
            return y

    # 併合
    def unite(self, x, y, w):
        rx = self.find(x)
        ry = self.find(y)
        # xの木の高さ < yの木の高さ
        if self.rank[rx] < self.rank[ry]:
            self.par[rx] = ry
            self.weight[rx] = w - self.weight[x] + self.weight[y]
        # xの木の高さ ≧ yの木の高さ
        else:
            self.par[ry] = rx
            self.weight[ry] = -w - self.weight[y] + self.weight[x]
            # 木の高さが同じだった場合の処理
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1

    # 同じ集合に属するか
    def same(self, x, y):
        return self.find(x) == self.find(y)

    # xからyへのコスト
    def diff(self, x, y):
        return self.weight[x] - self.weight[y]

"""
尺取り法

しゃくとり法は

- 「条件」を満たす区間 (連続する部分列) のうち、最小の長さを求める
- 「条件」を満たす区間 (連続する部分列) のうち、最大の長さを求める
- 「条件」を満たす区間 (連続する部分列) を数え上げる

といったことを効率良く実現できる。「条件を満たす区間」が以下のいずれかの構造になっている場合には
しゃくとり法を適用することができる。区間は半開区間「[l,r)」で考える

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

# lのGCD
def gcdlist(l):
    res = l[0]
    for i in range(1,len(l)):
        res = gcd(res, l[i])
    return res

def lcm(a,b):
    return a*b//gcd(a,b)

def lcmlist(l):
    res = l[0]
    for x in l[1:]:
        res = lcm(res, x)
    return res

# ax + by = cの整数解を求める
# cはgcd(a,b)の倍数である必要あり
# x,y = extGcd(a,b)で「ax+by=gcd(a,b)」が求まるのでc//gcd(a,b)倍する
def extGcd(a,b):
    if b==0:
        return 1, 0
    y,x = extGcd(b, a%b)
    y -= a//b * x
    return x,y

def isPrime(x):
    if x%2==0:
        return False
    a = 3
    while x>=a*a:
        if x%a==0:
            return False
        a += 2
    return True

def primeFactors(n):
    res = []
    while n%2==0:
        res.append(2)
        n //= 2
    x = 3
    while n>1 and n>=x*x:
        while n%x==0:
            res.append(x)
            n //= x
        x += 2
    if n>1:
        res.append(n)
    return res

# エラトステネスの篩
# 配列にはその添字の素因数のうち最小のものが入っている
def sieve(n):
    n += 10 # nが小さい時よう
    res = list(range(n))
    res[0] = -1
    res[1] = -1
    i = 2
    while i*i<n:
        if res[i]<i:
            i += 1
            continue
        j = i*i
        while j<n:
            if res[j]==j:
                res[j] = i
            j += i
        i += 1
    return res
# 以下のような感じでmの約数を数えられる
l = sieve(n)
r = 1
while m!=1:
    p = l[m]
    c = 0
    while l[m]==p:
        m //= l[m]
        c += 1
    r *= c+1

# 二分探索
### bisect.bisect_leftを使うことも検討する
def lower_bound(al, key):
    """
    一般に左側が満たしておらず、右側は満たしている判定基準(境目は一つ)ならlower_boundになる
    (条件を満たすもののうち、最小のインデックスを返す)
    単調にさえなっていれば、左右が逆になっていても検索には使える(ng/okも一緒に逆にする必要がある)
    """
    def isOk(a):
        # alの中でkey以上のアイテムのうち最小のインデックスを返す
        # upper_boundにする時にはa>key
        return a>=key

    ng = -1
    ok = len(al)

    while abs(ok-ng)>1:
        mid = (ok+ng)//2

        if isOk(al[mid]):
            ok = mid
        else:
            ng = mid

    return ok

# 最長増加部分列
def lis(al):
    n = len(al)
    dp = [10**9]*(n+1)

    for a in al:
        dp[lower_bound(dp, a)] = a
    return lower_bound(dp, 10**9)

# セグメント木
class SegTree:
    """docstring for SegTree."""
    def __init__(self, l, _n, u, f):
        n = 1
        while n<_n:
            n *= 2
        self.n = n
        self.dat = [u for _ in range(2*n)]
        self.u = u
        self.f = f
        for i in range(_n):
            self.dat[i+n-1] = l[i]
        self.init(0)

    def init(self, i):
        if i>=self.n-1:
            return self.dat[i]
        self.dat[i] = self.f(
            self.init(self.left(i)),
            self.init(self.right(i))
        )
        return self.dat[i]

    def par(self, i):
        return (i-1)//2

    def left(self, i):
        return 2*i+1

    def right(self, i):
        return 2*i+2

    def update(self, i, x):
        i += self.n-1
        self.dat[i] = x
        while i>0:
            i = self.par(i)
            self.dat[i] = self.f(
                self.dat[self.left(i)],
                self.dat[self.right(i)]
            )

    def q(self,a,b,k,l,r):
        if r<=a or b<=l:
            return self.u
        if a<=l and r<=b:
            return self.dat[k]
        return min(
            self.q(a,b,self.left(k),l,(l+r)//2),
            self.q(a,b,self.right(k),(l+r)//2,r)
        )

    def query(self,a,b):
        return self.q(a,b,0,0,self.n)

class BIT:
    def __init__(self, n):
        self.n = n
        self.l = [0]*(n+1)

    def add(self, idx, w):
        i = idx
        while i<=self.n:
            self.l[i] += w
            i += i&-i

    def sum(self, idx):
        res = 0
        i = idx
        while i>0:
            res += self.l[i]
            i -= i&-i
        return res

    def lower_bound(self, w):
        if w<=0:
            return 0
        idx = 0
        k = 1
        while k*2<=self.n:
            k *= 2
        while k>0:
            if idx+k<=self.n and self.l[idx+k]<w:
                w -= self.l[idx+k]
                idx += k
            k //= 2
        return idx+1

    def pos(self, idx):
        return self.sum(idx) - self.sum(idx-1)

    def array(self):
        res = []
        for i in range(1,self.n+1):
            res.append(self.pos(i))
        return res

# 巡回セールスマン問題のメモ可再帰版
# O(2^n*n^2)でn=16くらいまで
dp = [[-1]*n for _ in range(1<<n)]
dist = [[0] for _ in range(n)]

def dfs(s,v):
    if dp[s][v] >= 0:
        return dp[s][v]
    
    if s == (1<<n)-1 and v==0:
        dp[s][v] = 0
        return 0
    
    ans = 10**18
    for u in range(n):
        if not (s>>u & 1):
            ans = min(ans, dfs(s | 1<<u, u) + dist[v][u])
        
    dp[s][v] = ans
    return ans
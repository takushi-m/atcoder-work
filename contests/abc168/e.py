from collections import defaultdict
def gcd(a,b):
    while b!=0:
        a,b = b,a%b
    return a

def calc(m):
    x = ((pow(2,m,mod) + mod - 1)%mod + mod - m)%mod
    y = pow(2,n-m,mod)
    return (x*y)%mod


mod = 10**9+7
n = int(input())

ab = set()
d = defaultdict(lambda:0)
zz = 0
pz = 0
zp = 0
for _ in range(n):
    a,b = map(int, input().split())
    if a==0 and b==0:
        zz += 1
    elif a==0:
        zp += 1
    elif b==0:
        pz += 1
    else:
        a2 = abs(a)
        b2 = abs(b)
        g = gcd(a2,b2)
        d[(a//g, b//g)] += 1
        ab.add((a//g,b//g))

res = pow(2,n,mod)
res = (res + mod - 1)%mod
if zz>0:
    r = calc(zz)
    res = (res + mod - r)%mod
if zp+pz>0:
    r = calc(zp+pz)
    res = (res + mod - r)%mod

for a,b in ab:
    if a>0 and b>0:
        c = d[(b,-a)] + d[(-a,b)]
        if c>0:
            r = calc(c+1)
            res = (res + mod - r)%mod
    


print(res)
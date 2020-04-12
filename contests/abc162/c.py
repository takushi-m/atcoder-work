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

n = int(input())
res = 0

for i in range(1,n+1):
    for j in range(1,n+1):
        g = gcd(i,j)
        for k in range(1,n+1):
            res += gcd(g,k)
print(res)
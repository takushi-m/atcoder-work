from collections import Counter

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

n = int(input())
pl = primeFactors(n)

res = 0
cd = Counter(pl)
for k in cd:
    c = cd[k]
    i = 1
    while c-i>=0:
        c -= i
        res += 1
        i += 1
print(res)

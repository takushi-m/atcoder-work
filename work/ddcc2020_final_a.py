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
al = list(map(int, input().split()))

res = 0
for a in al:
    res = res^len(primeFactors(a))
if res==0:
    print("No")
else:
    print("Yes")
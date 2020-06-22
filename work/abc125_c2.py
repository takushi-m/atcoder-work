n = int(input())
al = list(map(int, input().split()))

def gcd(a,b):
    while b>0:
        a,b = b,a%b
    return a


accl = [0]*(n+1)
accr = [0]*(n+1)

accl[0] = al[0]
for i in range(n):
    accl[i+1] = gcd(accl[i],al[i])

accr[n] = al[n-1]
for i in range(n,0,-1):
    accr[i-1] = gcd(accr[i],al[i-1])

res = 0
for i in range(n):
    if i==0:
        res = max(res, accr[1])
    elif i==n-1:
        res = max(res, accl[n-1])
    else:
        res = max(res, gcd(accl[i], accr[i+1]))
print(res)
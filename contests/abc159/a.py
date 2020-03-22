n,m = map(int, input().split())

if n==0:
    res = m*(m-1)//2
elif m==0:
    res = n*(n-1)//2
else:
    res = n*(n-1)//2 + m*(m-1)//2

print(res)
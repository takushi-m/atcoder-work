n,a,b = map(int, input().split())

res = (n//(a+b))*a
n %= a+b
res += min(n,a)

print(res)
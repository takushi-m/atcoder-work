n = int(input())

res = 0
for j in range(1,n+1):
    x = n//j
    res += j*(1+x)*x//2

print(res)
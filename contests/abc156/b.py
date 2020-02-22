n,k = map(int, input().split())
res = 1
while not (k**(res-1)<=n<k**res):
    res += 1
print(res)
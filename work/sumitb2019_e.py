mod = 10**9+7
n = int(input())

res = 1
l = [0]*(n+1)
l[0] = 3
for a in list(map(int, input().split())):
    if l[a]<l[a+1]:
        print(0)
        exit()
    res = (res*(l[a] - l[a+1]))%mod
    l[a+1] += 1
print(res)
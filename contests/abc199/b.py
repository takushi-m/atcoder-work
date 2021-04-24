n = int(input())
al = list(map(int, input().split()))
bl = list(map(int, input().split()))

res = set(range(1,1000+1))
for i in range(n):
    a,b = al[i],bl[i]
    res &= set(range(a,b+1))

print(len(res))
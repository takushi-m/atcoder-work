n,k = map(int, input().split())
al = list(map(int, input().split()))
al = [(al[i],i) for i in range(n)]

d = {}
al2 = sorted(al)
for i in range(n):
    d[al2[i][1]] = i

r = k//n
k2 = k%n

for a,i in al:
    if d[i]<k2:
        print(r+1)
    else:
        print(r)
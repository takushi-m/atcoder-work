n = int(input())
al = list(map(int, input().split()))

d = [0]*n
for i in range(n):
    d[al[i]-1] += 1

s = 0
for i in range(n):
    if d[i]>1:
        s += d[i]*(d[i]-1)//2

for k in range(n):
    a = al[k]-1
    if d[a]<2:
        print(s)
        continue
    if d[a]==2:
        print(s-1)
        continue
    res = s - d[a]*(d[a]-1)//2 + (d[a]-1)*(d[a]-2)//2
    print(res)
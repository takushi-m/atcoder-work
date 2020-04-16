n,m,x = map(int, input().split())
al = list(map(int, input().split()))

for i in range(m):
    if al[i]>x:
        print(min(i, m-i))
        break
n,x = map(int, input().split())
al = list(map(int, input().split()))

res = 0
for i in range(n-1):
    a1 = al[i]
    a2 = al[i+1]
    if a1+a2>x:
        d = a1+a2-x
        res += d
        if a2>=d:
            al[i+1] -= d
        else:
            al[i+1] = 0

print(res)
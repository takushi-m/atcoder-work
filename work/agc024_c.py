n = int(input())
al = [int(input()) for _ in range(n)]

res = 0
i = n-1
while i>=0:
    j = i
    while j-1>=0 and al[j]==al[j-1]+1:
        j -= 1
    res += al[i]
    if al[j]>j:
        print(-1)
        exit()
    if j-1>=0 and al[j-1]<al[j]:
        print(-1)
        exit()
    i = j-1
print(res)


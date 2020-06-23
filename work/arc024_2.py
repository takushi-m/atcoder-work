n = int(input())
cl = [int(input()) for _ in range(n)]

if max(cl)==min(cl):
    print(-1)
    exit()
cl = cl + cl

res = 0
i = 0
while i<n:
    j = i
    while j<2*n and cl[i]==cl[j]:
        j += 1

    res = max(res, (j-i+1)//2)
    i = j
print(res)
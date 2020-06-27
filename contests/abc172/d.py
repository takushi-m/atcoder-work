def sieve(n):
    res = list(range(n+10)) # nが小さい時よう
    res[0] = -1
    res[1] = -1
    i = 2
    while i*i<n:
        if res[i]<i:
            i += 1
            continue
        j = i*i
        while j<n:
            if res[j]==j:
                res[j] = i
            j += i
        i += 1
    return res

n = int(input())
pl = []
for i,p in enumerate(sieve(n)):
    if i<n and p==i:
        pl.append(i)
print(pl)
l = [1]*(n+1)
l[0] = 0
l[1] = 0

i = 2
while i<=n:
    for j in pl:
        if i*j<=n:
            print(i,j)
            l[i*j] += l[i]
    i += 1

print(l)
print(sum(k*(l[k]+1) for k in range(n+1)))
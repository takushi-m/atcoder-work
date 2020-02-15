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

s = sieve(10**5+10)
acc = [0]*(10**5+10)
for i in range(2,10**5+9):
    if i%2==1 and s[i]==i and s[(i+1)//2]==(i+1)//2:
        acc[i+1] = acc[i]+1
    else:
        acc[i+1] = acc[i]

q = int(input())
res = [0]*q
for i in range(q):
    l,r = map(int, input().split())
    res[i] = acc[r+1]-acc[l]

for r in res:
    print(r)

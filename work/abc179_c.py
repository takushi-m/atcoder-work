def sieve(n):
    n += 10 # nが小さい時よう
    res = list(range(n))
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

l = sieve(n)
def calc(m):
    r = 1
    while m!=1:
        p = l[m]
        c = 0
        while l[m]==p:
            m //= l[m]
            c += 1
        r *= c+1
    return r

res = 0
for c in range(1,n):
    x = n - c
    res += calc(x)
print(res)

n = int(input())

def sieve(n):
    n += 10
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

l = sieve(n)
res = 0
for k in range(1,n+1):
    m = k
    r = 1
    while m!=1:
        p = l[m]
        c = 0
        while l[m]==p:
            m //= l[m]
            c += 1
        r *= c+1
    res += k*r
print(res)

n,k = map(int, input().split())
al = [int(input()) for _ in range(n)]

if 0 in al:
    print(n)
    exit()

r = 0
l = 0
m = 1
res = 0
while l<n:
    while r<n and m*al[r]<=k:
        m *= al[r]
        r += 1
    
    res = max(res, r-l)
    
    if r==l:
        r += 1
    else:
        m //= al[l]
    
    l += 1

print(res)
n = int(input())
al = list(map(int, input().split()))

s = set()
res = 0
l = r = 0
while l<n:
    while r<n and al[r] not in s:
        s.add(al[r])
        r += 1

    res = max(res, r-l)

    if r==l:
        r += 1
    else:
        s.remove(al[l])

    l += 1

print(res)
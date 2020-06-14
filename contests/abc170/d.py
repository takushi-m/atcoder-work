def check(s, a, next):
    if a==next:
        return False
    x = 1
    while a>=x*x:
        if a%x==0:
            if x in s:
                return False
            if a//x in s:
                return False
        x += 1
    return True

n = int(input())
al = list(map(int, input().split()))
al.sort()

s = set()
res = 0
for i in range(n):
    a = al[i]
    next = -1
    if i<n-1:
        next = al[i+1]
    if check(s,a,next):
        res += 1
    s.add(a)
print(res)


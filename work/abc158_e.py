from collections import defaultdict
n,p = map(int, input().split())
s = input()

if p==2 or p==5:
    res = 0
    for i in range(n-1,-1,-1):
        if int(s[i])%p==0:
            res += i+1
    print(res)
    exit()

u = defaultdict(int)
u[0] = 1
f = 1
d = 0
for i in range(n-1,-1,-1):
    d = (d + int(s[i])*f)%p
    f = (f*10)%p
    u[d%p] += 1

res = 0
for v in u.values():
    res += v*(v-1)//2

print(res)
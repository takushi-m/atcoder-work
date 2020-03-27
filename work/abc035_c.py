n,q = map(int, input().split())
m = [0]*(n+1)

for _ in range(q):
    a,b = map(int, input().split())
    a -= 1
    b -= 1
    m[a] += 1
    m[b+1] -= 1

res = [0]*n
s = 0
for i in range(n):
    s += m[i]
    s %= 2
    res[i] = s

print("".join(map(str,res)))
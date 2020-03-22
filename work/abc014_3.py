l = [0]*(10**6+10)
n = int(input())
for _ in range(n):
    a,b = map(int, input().split())
    l[a] += 1
    l[b+1] -= 1

r = 0
c = 0
for x in l:
    c += x
    r = max(r,c)

print(r)
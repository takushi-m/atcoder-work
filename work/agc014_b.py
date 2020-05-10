n,m = map(int, input().split())
d = [0]*n
for _ in range(m):
    a,b = map(int, input().split())
    d[a-1] += 1
    d[b-1] += 1

for x in d:
    if x%2==1:
        print("NO")
        exit()
print("YES")
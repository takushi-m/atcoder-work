n = int(input())
lb = [int(input()) for _ in range(n)]

l = [0]*n
for i in range(n-1):
    l[i+1] = l[i]^lb[i]

if l[n-1]^lb[n-1]==0:
    for a in l:
        print(a)
else:
    print(-1)
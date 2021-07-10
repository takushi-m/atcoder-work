n,x = map(int, input().split())
al = list(map(int, input().split()))

s = 0
for i in range(n):
    s += al[i]
    if i%2==1:
        s -= 1

if s<=x:
    print("Yes")
else:
    print("No")

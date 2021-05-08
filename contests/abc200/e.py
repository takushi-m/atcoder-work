n,k = map(int, input().split())

s=3
c=1
while True:
    if k-c<0:
        break

    s += 1
    c *= 3

s -= 1
c //= 3
k2 = k-c
print(s,k2)
for x in range(1,n+1):
    for y in range(1,n+1):
        z = s-x-y
        if n>=z>0:
            print(x,y,z)
            exit()

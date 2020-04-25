n,a,b = map(int, input().split())

if a>b:
    print(0)
    exit()
if n==1:
    if b-a>0:
        print(0)
    else:
        print(1)
    exit()
if n==2:
    print(1)
    exit()

res = (a+b*(n-1)) - (a*(n-1)+b) + 1
print(res)
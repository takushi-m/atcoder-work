k = int(input())
if k==1:
    print(1,1)
    exit()

b = 0
a = 1
for _ in range(k+1):
    a,b = a+b,a

print(a,b)

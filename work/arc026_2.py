n = int(input())
if n<5:
    print("Deficient")
    exit()

s = 1
if n%2==0:
    s += 2 + n//2
x = 3
while n>=x*x:
    if n%x==0:
        s += x
        m = n//x
        if x!=m:
            s += m
    x += 1

# print(s)
if s==n:
    print("Perfect")
elif s<n:
    print("Deficient")
else:
    print("Abundant")
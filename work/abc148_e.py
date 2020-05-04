n = int(input())

if n%2==1:
    print(0)
    exit()

n //= 2
res = 0
while n>0:
    res += n//5
    n //= 5

print(res)
d,n = map(int, input().split())
d = 100**d

x = 1
while n>0:
    if x%d==0 and (x//d)%100>0:
        n -= 1
    x += 1
print(x-1)
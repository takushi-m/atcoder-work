from math import floor

a,b = map(int, input().split())

for x in range(1,10**5):
    ax = floor(x*0.08)
    bx = floor(x*0.1)
    if ax==a and bx==b:
        print(x)
        exit()
print(-1)
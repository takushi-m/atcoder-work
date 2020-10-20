x,y,a,b = map(int, input().split())

res = 0
r = 0
while x<y:
    res = max(res, (y-x-1)//b + r)
    r += 1
    x *= a

print(res)
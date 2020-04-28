w,h,n = map(int, input().split())

x1,x2,y1,y2 = 0,w,0,h
for _ in range(n):
    x,y,a = map(int, input().split())
    if a==1:
        x1 = max(x1,x)
    elif a==2:
        x2 = min(x2,x)
    elif a==3:
        y1 = max(y1,y)
    else:
        y2 = min(y2,y)

if x1>=x2:
    print(0)
    exit()
if y1>=y2:
    print(0)
    exit()

print((x2-x1)*(y2-y1))
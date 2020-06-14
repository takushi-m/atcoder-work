x,y = map(int, input().split())

for t in range(x+1):
    k = x-t
    if y==t*2+k*4:
        print("Yes")
        exit()
print("No")
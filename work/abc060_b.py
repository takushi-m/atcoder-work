a,b,c = map(int, input().split())

for i in range(1,1000):
    if a*i%b==c:
        print("YES")
        exit()
print("NO")
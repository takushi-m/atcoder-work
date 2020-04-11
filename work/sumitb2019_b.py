n = int(input())

for x in range(1,n+1):
    if n==int(x*1.08):
        print(x)
        exit()
print(":(")
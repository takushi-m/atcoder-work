x = int(input())

n = 10**3
for a in range(-n,n):
    for b in range(-n,n):
        if a**5-b**5==x:
            print(a,b)
            exit()
n = int(input())
al = list(map(int, input().split()))

for a in al:
    if a%2==0:
        if a%3==0 or a%5==0:
            pass
        else:
            print("DENIED")
            exit()
print("APPROVED")
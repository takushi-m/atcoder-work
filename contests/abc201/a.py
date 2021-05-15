al = list(map(int, input().split()))

al.sort()
if al[0]-al[1]==al[1]-al[2]:
    print("Yes")
else:
    print("No")


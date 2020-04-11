n,a,b = map(int, input().split())
s = list(input())

sa = 0
sb = 0
for i in range(n):
    if s[i]=="a":
        if sa+sb<a+b:
            print("Yes")
            sa += 1
        else:
            print("No")
    elif s[i]=="b":
        if sa+sb<a+b and sb<b:
            print("Yes")
            sb += 1
        else:
            print("No")
    else:
        print("No")
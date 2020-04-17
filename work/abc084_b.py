a,b = map(int, input().split())
s = input()

if "-" in s[:a] or "-" in s[a+1:] or s[a]!="-":
    print("No")
else:
    print("Yes")
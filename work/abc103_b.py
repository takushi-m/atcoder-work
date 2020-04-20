s = input()
t = input()
n = len(s)

for i in range(n):
    if s[i:]+s[:i]==t:
        print("Yes")
        exit()
print("No")
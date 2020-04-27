n,a,b,c,d = map(int, input().split())
s = input()
a -= 1
b -= 1
c -= 1
d -= 1


if c<d:
    for i in range(b,d):
        if s[i]==s[i+1]=="#":
            print("No")
            exit()
    for i in range(a,c):
        if s[i]==s[i+1]=="#":
            print("No")
            exit()
    print("Yes")
    exit()

flag = False
for i in range(b-1,d):
    if s[i]==s[i+1]==s[i+2]==".":
        flag = True
        break
if not flag:
    print("No")
    exit()

for i in range(b,d):
    if s[i]==s[i+1]=="#":
        print("No")
        exit()
for i in range(a,c):
    if s[i]==s[i+1]=="#":
        print("No")
        exit()
print("Yes")
al = [input().split() for _ in range(3)]
n = int(input())
for _ in range(n):
    b = input()
    for i in range(3):
        for j in range(3):
            if al[i][j]==b:
                al[i][j] = "0"

if al[0][0]=="0" and al[0][1]=="0" and al[0][2]=="0":
    print("Yes")
elif al[1][0]=="0" and al[1][1]=="0" and al[1][2]=="0":
    print("Yes")
elif al[2][0]=="0" and al[2][1]=="0" and al[2][2]=="0":
    print("Yes")
elif al[0][0]=="0" and al[1][0]=="0" and al[2][0]=="0":
    print("Yes")
elif al[0][1]=="0" and al[1][1]=="0" and al[2][1]=="0":
    print("Yes")
elif al[0][2]=="0" and al[1][2]=="0" and al[2][2]=="0":
    print("Yes")
elif al[0][0]=="0" and al[1][1]=="0" and al[2][2]=="0":
    print("Yes")
elif al[0][2]=="0" and al[1][1]=="0" and al[2][0]=="0":
    print("Yes")
else:
    print("No")
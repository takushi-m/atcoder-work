# coding=utf-8

n = int(input())
n4 = 0
n2 = 0
n1 = 0
for x in input().split(" "):
    x = int(x)
    if x%4==0:
        n4 += 1
    elif x%2==0:
        n2 += 1
    else:
        n1 += 1

if n2>1:
    n2 = 1

if n1+n2-1<=n4:
    print("Yes")
else:
    print("No")

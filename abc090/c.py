# coding=utf-8
line = input().split(" ")
n = int(line[0])
m = int(line[1])

if n==1:
    if m==1:
        print(1)
    elif m==2:
        print(0)
    else:
        print(m-2)
    exit()
if m==1:
    if n==1:
        print(1)
    elif n==2:
        print(0)
    else:
        print(n-2)
    exit()

print((n-2)*(m-2))

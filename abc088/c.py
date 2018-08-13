# coding=utf-8

c = []

for _ in range(3):
    line = list(map(lambda x:int(x), input().split(" ")))
    c.append(line)

if not (c[0][0]-c[1][0] == c[0][1]-c[1][1] == c[0][2]-c[1][2]):
    print("No")
    exit()

if not (c[1][0]-c[2][0] == c[1][1]-c[2][1] == c[1][2]-c[2][2]):
    print("No")
    exit()

if not (c[2][0]-c[0][0] == c[2][1]-c[0][1] == c[2][2]-c[0][2]):
    print("No")
    exit()

if not (c[0][0]-c[0][1] == c[1][0]-c[1][1] == c[2][0]-c[2][1]):
    print("No")
    exit()

if not (c[0][1]-c[0][2] == c[1][1]-c[1][2] == c[2][1]-c[2][2]):
    print("No")
    exit()

if not (c[0][2]-c[0][0] == c[1][2]-c[1][0] == c[2][2]-c[2][0]):
    print("No")
    exit()

print("Yes")

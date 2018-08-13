# coding=utf-8

n = int(input())
m = 0
a = 0
r = 0
c = 0
h = 0

for _ in range(n):
    line = input()
    if line[0]=="M":
        m += 1
    elif line[0]=="A":
        a += 1
    elif line[0]=="R":
        r += 1
    elif line[0]=="C":
        c += 1
    elif line[0]=="H":
        h += 1

ret = m*a*r +m*a*c +m*a*h +m*r*c +m*r*h +m*c*h +a*r*c +a*r*h +a*c*h +r*c*h

print(ret)

# -*- coding: utf-8 -*-

c = []
for _ in range(3):
    line = list(map(int, input().split()))
    c.append(line)

for a1 in range(max(c[0])+1):
    for a2 in range(max(c[1])+1):
        for a3 in range(max(c[2])+1):
            b1 = c[0][0] - a1
            b2 = c[1][1] - a2
            b3 = c[2][2] - a3
            if a1+b1!=c[0][0]:
                continue
            if a1+b2!=c[0][1]:
                continue
            if a1+b3!=c[0][2]:
                continue
            if a2+b1!=c[1][0]:
                continue
            if a2+b2!=c[1][1]:
                continue
            if a2+b3!=c[1][2]:
                continue
            if a3+b1!=c[2][0]:
                continue
            if a3+b2!=c[2][1]:
                continue
            if a3+b3!=c[2][2]:
                continue
            print("Yes")
            exit()
print("No")

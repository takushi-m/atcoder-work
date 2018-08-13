# -*- coding: utf-8 -*-

line = input().split(" ")
A = int(line[0])
B = int(line[1])
C = int(line[2])
X = int(line[3])
Y = int(line[4])

ret = 99999999999
for a in range(X+1):
    t = a*A
    t += (X-a)*2*C
    if Y-(X-a)>0:
        t += (Y-(X-a))*B

    if t<ret:
        ret = t

for b in range(Y+1):
    t = b*B
    t += (Y-b)*2*C
    if X-(Y-b)>0:
        t += (X-(Y-b))*A

    if t<ret:
        ret = t
print(ret)

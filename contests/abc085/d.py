# coding=utf-8
from math import ceil

line = input().split(" ")
N = int(line[0])
H = int(line[1])

a = []
b = []

for _ in range(N):
    line = input().split(" ")
    a.append(int(line[0]))
    b.append(int(line[1]))

a.sort(reverse=True)
b.sort(reverse=True)

ret = 0
for x in b:
    if x<a[0]:
        break
    H -= x
    ret += 1
    if H<=0:
        break

if H>0:
    ret += ceil(H/a[0])

print(ret)

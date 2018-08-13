# coding=utf-8

line = input().split(" ")
n = int(line[0])
m = int(line[1])

x = 0
line1 = input().split(" ")
for (k,nn) in enumerate(line1):
    nn = int(nn)
    x += k*nn - (n-k-1)*nn


y = 0
line2 = input().split(" ")
for (k,nn) in enumerate(line2):
    nn = int(nn)
    y += k*nn - (m-k-1)*nn

print((x*y)%(10**9+7))

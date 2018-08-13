# coding=utf-8

line = input().split(" ")
N = int(line[0])
K = int(line[1])

n = (K-1)*(N-K)*2
n = 3*n
n += (N-1)*3
n += 1

print(n/N**3)

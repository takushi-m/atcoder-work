# coding=utf-8

line = input().split(" ")
n = int(line[0])
k = int(line[1])

ret = 0
for b in range(1,n+1):
    ret += n//b*max(b-k, 0) + max(n%b-k+1, 0)
    if 0%b>=k:
        ret -= 1

print(ret)

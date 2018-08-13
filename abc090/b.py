# coding=utf-8

line = input().split(" ")
a = int(line[0])
b = int(line[1])

def judge(n):
    n = str(n)
    return n == (n[::-1])

ret = 0
for n in range(a,b+1):
    if judge(n):
        ret += 1

print(ret)

# coding=utf-8

A = int(input())
B = int(input())
C = int(input())
X = int(input())

ret = 0
for a in range(0,A+1):
    for b in range(0,B+1):
        for c in range(0,C+1):
            s = 500*a+100*b+c*50
            if s==X:
                ret += 1

print(ret)

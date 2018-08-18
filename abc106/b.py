# -*- coding: utf-8 -*-

n = int(input())

def judge(x):
    ret = 1
    for i in range(1,x):
        if x%i==0:
            ret += 1
    return ret

ret = 0
for i in range(1,n+1):
    if i%2==1 and judge(i)==8:
        ret += 1
print(ret)

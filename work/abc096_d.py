# -*- coding: utf-8 -*-
N = int(input())

prime = [2]
for n in range(3,55555+1):
    flag = True
    for p in prime:
        if n%p==0:
            flag = False
            break
        if n<p*p:
            break
    if flag:
        prime.append(n)

ret = []
for n in prime:
    if len(ret)==N:
        break
    if n%5==1:
        ret.append(str(n))
print(" ".join(ret))

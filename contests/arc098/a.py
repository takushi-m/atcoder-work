# -*- coding: utf-8 -*-

n = int(input())
acc_e = [0]
acc_w = [0]

for (i,s) in enumerate(list(input())):
    if s=="W":
        acc_w.append(acc_w[i]+1)
        acc_e.append(acc_e[i])
    else:
        acc_w.append(acc_w[i])
        acc_e.append(acc_e[i]+1)

#print(acc_w)
#print(acc_e)

ret = 999999
for i in range(n):
    r = acc_w[i] + (acc_e[-1]-acc_e[i+1])
    if r<ret:
        ret = r

print(ret)

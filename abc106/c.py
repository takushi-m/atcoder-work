# -*- coding: utf-8 -*-
s = input()
k = int(input())

# g = 5000000000000000

ret = ""
for i,x in enumerate(s):
    # print(i,x)
    if x!="1":
        print(x)
        exit()
    elif i+1==k:
        print(1)
        exit()
print(1)

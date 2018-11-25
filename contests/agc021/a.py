# coding=utf-8
import re

n = input()
l = len(n)-1

def f(s):
    return sum(map(int, list(s)))

if l==0:
    print(n)
elif re.search("^9+$", n)!=None:
    print(9*(l+1))
else:
    r = max(f(n), 9*l + (int(n[0])-1))
    print(r)

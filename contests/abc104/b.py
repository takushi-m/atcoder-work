# -*- coding: utf-8 -*-
s = input()

flag = True

if s[0]!="A":
    print("WA")
    exit()

if "C" not in s[2:-1]:
    print("WA")
    exit()

idx = s[2:-1].find("C")+2

s = s[1:idx]+s[idx+1:]

if s == s.lower():
    print("AC")
else:
    print("WA")

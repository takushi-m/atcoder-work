# -*- coding: utf-8 -*-
s = input()

res = []

if 0<int(s[2:])<13: # YYMM
    res.append("YYMM")
if 0<int(s[:2])<13: # MMYY
    res.append("MMYY")

if len(res)==1:
    print(res[0])
elif len(res)==2:
    print("AMBIGUOUS")
else:
    print("NA")

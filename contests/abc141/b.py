# -*- coding: utf-8 -*-
s = input()

for i in range(len(s)):
    c = s[i]
    if (i+1)%2==1:
        if c not in ("R","U","D"):
            print("No")
            exit()
    else:
        if c not in ("L","U","D"):
            print("No")
            exit()
print("Yes")

# -*- coding: utf-8 -*-

s = input()[::-1]
w = [
    "dream"[::-1]
    ,"dreamer"[::-1]
    ,"erase"[::-1]
    ,"eraser"[::-1]
]

while len(s)>0:
    if s.startswith(w[0]):
        s = s[len(w[0]):]
    elif s.startswith(w[1]):
        s = s[len(w[1]):]
    elif s.startswith(w[2]):
        s = s[len(w[2]):]
    elif s.startswith(w[3]):
        s = s[len(w[3]):]
    else:
        break

if len(s)==0:
    print("YES")
else:
    print("NO")

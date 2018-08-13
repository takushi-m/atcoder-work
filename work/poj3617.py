# coding=utf-8

s = input()
t = ""

while len(s)>0:
    s2 = s[::-1]
    if s<s2:
        t += s[0]
        s = s[1:]
    else:
        t += s[-1]
        s = s[:-1]

print(t)

# -*- coding: utf-8 -*-
s = input()
k = "keyence"

pre = None
for i in range(1,7+1):
    if s[:i]==k[:i]:
        pre = i

if pre is None:
    print("NO")
elif pre==7:
    print("YES")
elif k[pre:]==s[-(7-pre):]:
    print("YES")
else:
    print("NO")

# -*- coding: utf-8 -*-
n = int(input())
s = input()

stack = []
for i in range(n):
    if s[i]=="(":
        stack.append("(")
    else:
        if len(stack)==0:
            stack.append(")")
        elif stack[-1]=="(":
            stack.pop()
        else:
            stack.append(")")

lcnt = 0
rcnt = 0
for c in stack:
    if c=="(":
        rcnt += 1
    else:
        lcnt += 1
print(("("*lcnt) + s + (")"*rcnt))

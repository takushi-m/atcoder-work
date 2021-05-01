from collections import deque

s = input()
l = deque([])
rev = True
for i in range(len(s)):
    if s[i]=="R":
        rev = not rev
    else:
        if rev:
            l.append(s[i])
        else:
            l.appendleft(s[i])

if not rev:
    l.reverse()

t = []
for c in l:
    if len(t)==0:
        t.append(c)
        continue
    if t[-1]==c:
        t.pop()
    else:
        t.append(c)

print("".join(t))

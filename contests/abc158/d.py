from collections import deque

s = deque(list(input()))
q = int(input())

asc = True
for _ in range(q):
    qs = input()
    if qs[0]=="1":
        asc = not asc
        continue

    _,f,c = qs.split()
    if f=="1":
        if asc:
            s.appendleft(c)
        else:
            s.append(c)
    else:
        if asc:
            s.append(c)
        else:
            s.appendleft(c)

if not asc:
    s.reverse()
print("".join(s))
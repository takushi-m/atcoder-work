n = int(input())
res = 0
c = n

for _ in range(n):
    s = input()
    cc = -1
    for i in range(c):
        if s[i]==".":
            cc = i
    if cc>=0:
        c = cc
        res += 1
    else:
        c = n

print(res)

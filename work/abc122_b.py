s = input()
n = len(s)

res = 0
for i in range(n):
    c = 0
    for j in range(i,n):
        if s[j] not in ("A","G","C","T"):
            break
        c += 1
    res = max(res, c)
print(res)
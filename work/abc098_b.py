n = int(input())
s = list(input())

res = 0
for i in range(n):
    s1 = set(s[:i])
    s2 = set(s[i:])

    res = max(res,len(s1&s2))
print(res)
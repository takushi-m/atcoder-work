from collections import defaultdict
s = input()
n = len(s)

d = defaultdict(int)
d[0] = 1
x = 0
b = 1
for i in range(n-1,-1,-1):
    x += b*int(s[i])
    x %= 2019
    d[x] += 1

    b *= 10
    b %= 2019

res = 0
for k in d:
    c = d[k]
    res += c*(c-1)//2
print(res)

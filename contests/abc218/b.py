pl = list(map(int, input().split()))
s = "abcdefghijklmnopqrstuvwxyz"
res = []

for p in pl:
    res.append(s[p-1])
print("".join(res))
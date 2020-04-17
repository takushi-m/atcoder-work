n = int(input())
s = input()

x = 0
res = 0
for op in list(s):
    if op=="I":
        x += 1
    else:
        x -= 1
    res = max(res, x)
print(res)
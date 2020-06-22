s = input()
gcnt = 0
pcnt = 0
res = 0

for c in s:
    if pcnt<gcnt:
        pcnt += 1
        if c=="g":
            res += 1
    else:
        gcnt += 1
        if c=="p":
            res -= 1
print(res)

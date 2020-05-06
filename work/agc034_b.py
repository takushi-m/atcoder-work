s = input()
n = len(s)

res = 0
ac = 0
i = 0
while i<n:
    if s[i]=="A":
        ac += 1
    elif s[i]=="B" and i+1<n and s[i+1]=="C":
        res += ac
        i += 1
    else:
        ac = 0
    i += 1
print(res)

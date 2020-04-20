o = input()
e = input()

res = []
for i in range(min(len(o),len(e))):
    res.append(o[i])
    res.append(e[i])
if len(o)>len(e):
    res.append(o[-1])

print("".join(res))
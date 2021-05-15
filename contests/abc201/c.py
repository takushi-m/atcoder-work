s = input()

e = set()
for n in range(10):
    if s[n]=="o":
        e.add(n)

res = 0
for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                ss = set([a,b,c,d])
                if not (ss >= e):
                    continue
            
                if s[a]=="x":
                    continue
                if s[b]=="x":
                    continue
                if s[c]=="x":
                    continue
                if s[d]=="x":
                    continue
                res += 1
print(res)
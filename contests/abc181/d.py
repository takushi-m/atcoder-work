from collections import Counter

s = input()
if len(s)==1:
    if int(s)%8==0:
        print("Yes")
    else:
        print("No")
    exit()
if len(s)==2:
    if int(s[1]+s[0])%8==0 or int(s[0]+s[1])%8==0:
        print("Yes")
    else:
        print("No")
    exit()

s = Counter(list(s))

res = set([])
for n in range(1,1000):
    if n%10==0 or (n//10)%10==0 or (n//100)%10==0:
        continue
    if n%8==0:
        res.add(n)
    

for u in res:
    c = Counter(str(u))
    flag = True
    for x in ["1","2","3","4","5","6","7","8","9"]:
        flag = flag and s[x]>=c[x]
    if flag:
        print("Yes")
        exit()
print("No")
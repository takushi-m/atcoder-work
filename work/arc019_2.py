s = input()
sr = s[::-1]
n = len(s)

if n==1:
    print(0)
    exit()
if s==sr:
    print(25*(n-n%2))
    exit()

d = 0
for i in range(n//2):
    if s[i]!=s[n-1-i]:
        d += 1

if d>1:
    print(25*n)
else:
    res = 25*(n-n%2-2)+24*2
    if n%2==1:
        res += 25
    print(res)

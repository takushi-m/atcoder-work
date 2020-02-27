s = input()
n = len(s)

res = n
for i in range(n-1):
    if s[i]!=s[i+1]:
        res = min(res, max(i+1,n-(i+1)))

print(res)
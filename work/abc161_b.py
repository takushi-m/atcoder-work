n,m = map(int, input().split())
al = list(map(int, input().split()))

s = sum(al)
t = s/(4.0*m)
res = 0
for a in al:
    if a>=t:
        res += 1

if res>=m:
    print("Yes")
else:
    print("No")
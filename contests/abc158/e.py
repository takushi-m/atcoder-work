n,p = map(int, input().split())
s = input()
sn = int(s)

res = 0
x = 1
while p*x<=sn:
    res += s.count(str(p*x))
    x += 1

print(res)
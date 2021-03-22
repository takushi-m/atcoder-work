ns = input()
n = int(ns)

l = len(ns)//2
N = 10**l
cnt = 0

x = 1
while x<N:
    m = int(str(x)*2)
    if m<=n:
        cnt += 1
    x += 1

print(cnt)

n = int(input())
dl = [int(input()) for _ in range(n)]

m = 0
for d in dl:
    m = max(m, d)

sd = sum(dl)
print(sd)
if m>sd-m:
    print(m-(sd-m))
else:
    print(0)
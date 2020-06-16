n = int(input())
if n==0:
    print(0)
    exit()
res = []
while n != 0:
    x = n%-2

    if x<0:
        res.append(1)
        n -= 1
        n //= -2
    else:
        res.append(0)
        n //= -2

res.reverse()
print("".join(str(c) for c in res))
from string import ascii_lowercase

n = int(input())
res = []

while n>0:
    c = n%26
    res.append(ascii_lowercase[c-1])
    if c==0:
        n = (n-26)//26
    else:
        n //= 26


res.reverse()
print("".join(res))

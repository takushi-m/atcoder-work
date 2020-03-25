n = int(input())
s = set()
for x in input().split():
    x = int(x)
    while x%2==0:
        x //= 2
    s.add(x)
print(len(s))
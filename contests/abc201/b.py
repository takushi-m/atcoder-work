n = int(input())
l = []
for _ in range(n):
    s,t = input().split()
    l.append((int(t),s))

l.sort()
print(l[-2][1])
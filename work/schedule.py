# coding=utf-8

n = int(input())
l = []

for _ in range(n):
    line = input().split(" ")
    l.append((int(line[0]), int(line[1])))

print(l)
l.sort(key=lambda c: c[1])
print(l)

t = 0
cnt = 0
for c in l:
    if c[0]>t:
        cnt += 1
        t = c[1]
        print(c)

print(c)

# coding=utf-8
line = input().split(" ")
n = int(line[0])
z = int(line[1])
w = int(line[2])

a = []
for x in input().split(" "):
    a.append(int(x))

print(max(abs(w-a[n-1]), abs(a[n-2]-a[n-1])))

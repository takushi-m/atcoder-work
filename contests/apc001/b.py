# coding=utf-8
N = int(input())
a = []
b = []

for x in input().split(" "):
    a.append(int(x))
for x in input().split(" "):
    b.append(int(x))

print(a)
print(b)

for i in range(N):
    if a[i]==b[i]:
        continue
    l = [(idx,b[idx] for idx in range(N))]
    l.sort(key=lambda x:x[1])
    for j in range(N):
        idx = l[j][0]
        val = l[j][1]
        if a[idx]==b[idx]
            continue
        

print(a)
print(b)

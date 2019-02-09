# -*- coding: utf-8 -*-
p = [0]*4

for _ in range(3):
    a,b = map(int, input().split())
    a -= 1
    b -= 1
    p[a] += 1
    p[b] += 1

odd = 0
even = 0
for x in p:
    if x%2==1:
        odd += 1
    else:
        even += 1

if even==4:
    print("YES")
elif odd==2:
    print("YES")
else:
    print("NO")

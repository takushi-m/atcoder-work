# -*- coding: utf-8 -*-
n = int(input())
al = list(map(int, input().split()))

x = al[-1]
for i in range(n-1):
    x += (-1)**(i+1) * al[i]
x //= 2
xl = [x]

for i in range(n-1):
    xl.append(al[n-i-2] - xl[i])

print(*reversed(list(map(lambda a:a*2, xl))))
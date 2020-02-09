# -*- coding: utf-8 -*-
n = int(input())
al = list(map(int, input().split()))


d = set()
for a in al:
    if a in d:
        print("NO")
        exit()
    d.add(a)

print("YES")
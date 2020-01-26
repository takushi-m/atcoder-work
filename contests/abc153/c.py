# -*- coding: utf-8 -*-
n,k = map(int, input().split())
hl = list(map(int, input().split()))

hl.sort(reverse=True)
hl = hl[k:]
print(sum(hl))
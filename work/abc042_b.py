# -*- coding: utf-8 -*-
n,k = map(int, input().split())
sl = [input() for _ in range(n)]

sl.sort()
print("".join(sl))
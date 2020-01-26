# -*- coding: utf-8 -*-
h,n = map(int, input().split())
al = list(map(int, input().split()))

if h<=sum(al):
    print("Yes")
else:
    print("No")
# -*- coding: utf-8 -*-
n,m = [int(x) for x in input().split()]

print((1900*m+100*(n-m))*(2**m))

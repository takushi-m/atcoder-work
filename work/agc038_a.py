# -*- coding: utf-8 -*-
h,w,a,b = map(int, input().split())

for hi in range(h):
    if hi<b:
        line = ["1"]*a + ["0"]*(w-a)
    else:
        line = ["0"]*a + ["1"]*(w-a)
    print("".join(line))
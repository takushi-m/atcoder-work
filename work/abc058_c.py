# -*- coding: utf-8 -*-

line = input().split(" ")
n = int(line[0])
k = int(line[1])
d = set(input().split(" "))

while True:
    s = set(list(str(n)))
    r = s - d
    if len(r)==len(s):
        print(n)
        exit()
    n += 1

# coding=utf-8

line = input().split(" ")
ret = {}

for w in line:
    if w in ret:
        ret[w] += 1
    else:
        ret[w] = 1

for w in line:
    if w in ret:
        print(w+" "+str(ret[w]))
        del ret[w]

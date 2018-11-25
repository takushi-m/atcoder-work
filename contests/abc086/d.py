# coding=utf-8
from pprint import pprint

line = input().split(" ")
N = int(line[0])
K = int(line[1])
l = []
for _ in range(N):
    line = input().split(" ")
    x = int(line[0])
    y = int(line[1])
    c = line[2]
    if c=="W":
        x += K
    l.append((x%(2*K),y%(2*K),"B"))

def count(x,y):
    # x,y が左下黒だとしていくつ希望を叶えているかカウントする
    ret = 0
    for p in l:
        xx = (p[0]-x+2*K)%(2*K)
        yy = (p[1]-y+2*K)%(2*K)
        if xx<K and yy<K:
            ret += 1
        elif xx>=K and yy>=K:
            ret += 1
    return ret

ret = -1
for x in range(2*K):
    for y in range(2*K):
        t = count(x,y)
        if t>ret:
            ret = t

print(ret)

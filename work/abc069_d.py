# coding=utf-8

line = input().split(" ")
h = int(line[0])
w = int(line[1])
n = int(input())
a = [int(x) for x in input().split(" ")]

c = []
for (i,x) in enumerate(a):
    c.extend([str(i+1) for _ in range(x)])

ret = []
for idx in range(h):
    if idx%2==0:
        ret.append(c[idx*w:(idx+1)*w])
    else:
        ret.append(sorted(c[idx*w:(idx+1)*w],reverse=True))

for i in range(h):
    print(" ".join(ret[i]))

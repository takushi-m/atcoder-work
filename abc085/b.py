# coding=utf-8

N = int(input())
mochi = []

for _ in range(N):
    mochi.append(int(input()))

mochi.sort(reverse=True)

ret = 1
for i in range(len(mochi)-1):
    if mochi[i]>mochi[i+1]:
        ret += 1

print(ret)

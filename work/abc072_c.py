# coding=utf-8
from collections import Counter

N = input()
line = input().split(" ")

cnt = Counter()
for i in line:
    x = int(i)
    cnt[x] += 1
    cnt[x-1] += 1
    cnt[x+1] += 1
print(cnt.most_common(1)[0][1])

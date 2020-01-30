# -*- coding: utf-8 -*-
import heapq

n = int(input())
al = list(map(int, input().split()))

q = []
heapq.heapify(q)
s = 0
for i in range(n):
    heapq.heappush(q, al[i])
    s += al[i]

red = [s]
for i in range(n,2*n):
    a = heapq.heappushpop(q, al[i])
    s = s - a + al[i]
    red.append(s)

q = []
heapq.heapify(q)
s = 0
for i in range(2*n,3*n):
    heapq.heappush(q, -al[i])
    s += al[i]

blue = [s]
for i in range(2*n-1,n-1,-1):
    a = heapq.heappushpop(q, -al[i])
    s = s + a + al[i]
    blue.append(s)

# print(red)
# print(blue)
res = red[0] - blue[-1]
for i in range(n+1):
    res = max(res, red[i] - blue[-1-i])

print(res)
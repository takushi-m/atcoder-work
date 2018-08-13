# coding=utf-8

import heapq

h = []
def push(n):
    heapq.heappush(h, -1*n)
def pop():
    return -1*heapq.heappop(h)
def empty():
    return len(h)==0

n = 4
l = 25
p = 10
a = [10,14,20,21]
b = [10,5,2,4]

ans = 0
pos = 0
tank = p

for i in range(n):
    d = a[i]-pos

    while tank<d:
        if empty():
            print("-1")
            exit()

        tank += pop()
        ans += 1

    tank -= d
    pos += d
    push(b[i])

print(ans)

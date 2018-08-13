# coding=utf-8

from queue import PriorityQueue

n = 3
l = [8,5,8]

q = PriorityQueue()
for x in l:
    q.put(x)

ans = 0
while q.qsize()>1:
    l1 = q.get()
    l2 = q.get()

    ans += l1+l2
    q.put(l1+l2)

print(ans)

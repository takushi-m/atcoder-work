from collections import deque

k = int(input())
q = deque()
for i in range(1,10):
    q.append(i)

for _ in range(k):
    a = q.popleft()
    d = a%10
    if d>0:
        q.append(10*a+d-1)
    q.append(10*a+d)
    if d<9:
        q.append(10*a+d+1)
print(a)
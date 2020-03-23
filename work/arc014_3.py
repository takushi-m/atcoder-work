from collections import deque

n = int(input())
s = list(input())

q = deque()
i = 0
while i<n:
    x = s[i]
    if len(q)==0:
        q.append(x)
    elif q[0]==x:
        q.popleft()
    elif q[-1]==x:
        q.pop()
    elif i==n-1:
        q.append(x)
    elif x==s[i+1]:
        i += 1
    elif q[0]==s[i+1]:
        q.append(x)
    else:
        q.appendleft(x)
    # print(i,q)
    i += 1
print(len(q))
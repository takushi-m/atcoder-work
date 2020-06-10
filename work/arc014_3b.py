from collections import deque

n = int(input())
sl = input()

q = deque([])
for i in range(n):
    s = sl[i]
    if len(q)==0:
        q.appendleft(s)
    elif q[0]==s and q[-1]!=s:
        q.popleft()
    elif q[0]!=s and q[-1]==s:
        q.pop()
    elif q[0]==s and q[-1]==s:
        q.pop()
    else:
        if i==n-1:
            q.append(s)
        else:
            s2 = sl[i+1]
            if q[0]==s2:
                q.append(s)
            else:
                q.appendleft(s)
print(len(q))
# coding=utf-8

N = int(input())

l = [(0,0,0)]
for _ in range(N):
    line = input().split(" ")
    t = int(line[0])
    x = int(line[1])
    y = int(line[2])
    l.append((t, x, y))

def judge(s1, s2):
    t = abs(s1[1]-s2[1])
    t += abs(s1[2]-s2[2])
    diff = (s2[0]-s1[0]) - t

    if diff==0:
        return True
    elif diff<0:
        return False
    else:
        return diff%2==0

for i in range(len(l)-1):
    s1 = l[i]
    s2 = l[i+1]
    if not judge(s1,s2):
        print("No")
        exit()
print("Yes")

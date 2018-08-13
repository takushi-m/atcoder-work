# coding=utf-8
line = input().split(" ")
n = int(line[0])
k = int(line[1])

pods = []
for _ in range(n):
    line = input().split(" ")
    pods.append((float(line[0]), float(line[1]))) # (w, p)

pods.sort(key=lambda c:c[1], reverse=True)

w = 0.0
salt = 0.0
for i in range(k):
    w += pods[i][0]
    salt += pods[i][0]*pods[i][1]/100.0

print(salt/w*100.0)

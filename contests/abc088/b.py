# coding=utf-8

N = int(input())
a = []

for x in input().split(" "):
    a.append(int(x))

a.sort(reverse=True)

alice = 0
bob = 0

for i in range(N):
    if i%2==0:
        alice += a[i]
    else:
        bob += a[i]

print(alice-bob)

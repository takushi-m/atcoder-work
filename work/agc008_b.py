# -*- coding: utf-8 -*-
n,k = map(int, input().split())
a = [int(x) for x in input().split()]

acc_a = []
acc_b = []
acc_a.append(0)
acc_b.append(0)

for i in range(n):
    acc_a.append(a[i]+acc_a[-1])
    acc_b.append(max(0,a[i]) + acc_b[-1])

ans = 0
for i in range(n-k+1):
    t = acc_a[i+k] - acc_a[i]
    t += acc_b[i] - acc_b[0]
    t += acc_b[n] - acc_b[i+k]
    ans = max(ans,t)

    t = 0
    t += acc_b[i] - acc_b[0]
    t += acc_b[n] - acc_b[i+k]
    ans = max(ans,t)
print(ans)

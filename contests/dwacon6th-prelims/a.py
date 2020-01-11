# -*- coding: utf-8 -*-
n = int(input())
st = []
for i in range(n):
    s,t = input().split()
    st.append([s,int(t)])
x = input()

res = 0
flag = False
for i in range(n):
    s,t = st[i]
    if flag:
        res += t
    elif s==x:
        flag = True

print(res)
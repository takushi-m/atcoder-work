# -*- coding: utf-8 -*-
s = list(input())
n = len(s)

st = []
res = 0
for i in range(n):
    if len(st)>0:
        top = st[-1]
        if s[i]!=top:
            res += 2
            st.pop()
        else:
            st.append(s[i])
    else:
        st.append(s[i])
print(res)

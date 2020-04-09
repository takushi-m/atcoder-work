s = input()
n = len(s)

res = 10**5
for c in set(list(s)):
    ss = list(s)
    cnt = 0
    while len(set(ss))>1:
        cnt += 1
        for i in range(len(ss)-1):
            if c==ss[i+1]:
                ss[i] = c
        ss.pop()
    res = min(res, cnt)

print(res)
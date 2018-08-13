n = int(input())
a = [int(x) for x in input().split(" ")]

s = [0 for _ in range(n)]
s[0] = abs(a[0])
for i in range(1,len(a)):
    s[i] = s[i-1] + abs(a[i]-a[i-1])
s.append(s[-1]+abs(a[-1]))

for i in range(n):
    if i==0:
        ret = abs(s[-1]-s[i+1]) + abs(a[i+1])
    elif i==len(a)-1:
        ret = s[i-1] + abs(a[i-1])
    else:
        ret = s[i-1] + abs(s[-1]-s[i+1]) + abs(a[i+1]-a[i-1])

    print(ret)

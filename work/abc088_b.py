n = int(input())
al = list(map(int, input().split()))
al.sort(reverse=True)
a = 0
b = 0
for i in range(n):
    if i%2==0:
        a += al[i]
    else:
        b += al[i]

print(a-b)
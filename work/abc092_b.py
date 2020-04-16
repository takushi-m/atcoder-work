n = int(input())
d,x = map(int, input().split())
al = [int(input()) for _ in range(n)]

res = 0
for i in range(1,d+1):
    for a in al:
        if (i-1)%a==0:
            res += 1
print(res+x)
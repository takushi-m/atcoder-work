n = int(input())
al = [int(s)-1 for s in input().split()]

res = 0
for i in range(n):
    if i==al[al[i]]:
        res += 1
print(res//2)
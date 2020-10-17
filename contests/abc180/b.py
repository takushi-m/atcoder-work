from math import sqrt
n = int(input())
xl = list(map(int, input().split()))

print(sum(map(abs, xl)))
print(sqrt(sum(map(lambda x:x*x, xl))))

r1 = 0
for x in xl:
    r1 = max(r1, abs(x))
print(r1)

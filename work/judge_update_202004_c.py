from itertools import permutations

al = list(map(int, input().split()))
n = sum(al)
xl = [
    list(range(al[0])),
    [al[0]+x for x in range(al[1])],
    [al[0]+al[1]+x for x in range(al[2])]
]

res = 0
for r in permutations(range(n), r=n):
    flag = True
    for i in range(3):
        for j in range(1,al[i]):
            if not r[xl[i][j]]>r[xl[i][j-1]]:
                flag = False
    for i in range(1,3):
        for j in range(al[i]):
            if not r[xl[i][j]]>r[xl[i-1][j]]:
                flag = False
    if flag:
        res += 1

print(res)
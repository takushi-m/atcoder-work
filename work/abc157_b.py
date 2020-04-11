al = [list(map(int, input().split())) for _ in range(3)]
n = int(input())

for _ in range(n):
    x = int(input())
    for i in range(3):
        for j in range(3):
            if al[i][j]==x:
                al[i][j] = -1

for i in range(3):
    if -3==sum(al[i]):
        print("Yes")
        exit()

    if -3==sum([al[j][i] for j in range(3)]):
        print("Yes")
        exit()

if al[0][0]+al[1][1]+al[2][2]==-3:
    print("Yes")
    exit()
if al[0][2]+al[1][1]+al[2][0]==-3:
    print("Yes")
    exit()

print("No")

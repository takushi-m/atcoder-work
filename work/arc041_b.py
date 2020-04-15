n,m = map(int, input().split())
bl = [list(map(int, list(input()))) for _ in range(n)]

al = [[0]*m for _ in range(n)]

for i in range(1,n-1):
    for j in range(1,m-1):
        x = bl[i-1][j]
        al[i][j] = x

        bl[i][j+1] -= x
        bl[i][j-1] -= x
        bl[i+1][j] -= x
        bl[i-1][j] -= x

for a in al:
    print("".join(map(str,a)))
n = int(input())
l = []
for _ in range(n):
    l.append(list(map(int, input().split())))

# 総合値t以上のチームを作れる
def check(t):
    # print(t)
    clear = [False]*5

    for _ in range(3):
        cnt = 0
        idx = -1
        for i in range(n):
            c = 0
            for j in range(5):
                if clear[j]:
                    continue
                x = l[i][j]
                if x>=t:
                    c += 1
            if c>cnt:
                cnt = c
                idx = i
        if cnt == 0:
            return False
        for i in range(5):
            if l[idx][i]>=t:
                clear[i] = True
        if all(clear):
            return True
    return all(clear)

ok = 1
ng = 10**9 + 1
while abs(ng-ok)>1:
    m = abs(ng+ok)//2
    if check(m):
        ok = m
    else:
        ng = m
print(ok)
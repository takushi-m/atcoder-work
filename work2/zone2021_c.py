n = int(input())
l = []
for _ in range(n):
    l.append(list(map(int, input().split())))

# 総合値t以上のチームを作れる
def check(t):
    s = set()
    for i in range(n):
        x = 0
        for j in range(5):
            if l[i][j]>=t:
                x += 1<<j
        if x>0:
            s.add(x)

    for x1 in s:
        for x2 in s:
            for x3 in s:
                if x1|x2|x3 == 31:
                    return True
    return False

ok = 1
ng = 10**9 + 1
while abs(ng-ok)>1:
    m = abs(ng+ok)//2
    if check(m):
        ok = m
    else:
        ng = m
print(ok)
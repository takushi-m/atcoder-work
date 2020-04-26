P = 2019
S = input()
N = len(S)
 
if P == 2 or P == 5:
    ans = 0
    for i in range(N):
        if int(S[i]) % P == 0:
            ans += i + 1
    print(ans)
    exit()
 
num = [0] * P
num[0] = 1
now, ans = 0, 0
_10 = 1
for i in range(N-1, -1, -1):
    now = (now + int(S[i]) * _10) % P
    _10 *= 10
    _10 %= P
    ans += num[now]
    num[now] += 1
 
print(ans)
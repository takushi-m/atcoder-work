h,w = map(int, input().split())

al = ["#"*(w+2)]
for _ in range(h):
    al.append("#"+input()+"#")
al.append("#"*(w+2))

for a in al:
    print(a)
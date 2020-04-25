n = int(input())
s = input()
t = input()

if s==t:
    print(n)
    exit()

for i in range(n):
    if s[i:]==t[:-i]:
        print(2*n-(n-i))
        exit()
print(2*n)

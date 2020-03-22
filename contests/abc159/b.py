s = input()
n = len(s)

if s!=s[::-1]:
    print("No")
    exit()

s2 = s[:(n-1)//2]
if s2!=s2[::-1]:
    print("No")
    exit()

s3 = s[(n+3)//2-1:]
if s3!=s3[::-1]:
    print("No")
    exit()

print("Yes")
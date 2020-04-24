s = input()

while True:
    s = s[:-1]
    n = len(s)
    if n%2==1:
        continue
    if s[:n//2]==s[n//2:]:
        print(n)
        exit()
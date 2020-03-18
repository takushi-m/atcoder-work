s = input()
if s=="{}":
    print("dict")
    exit()

p = 0
for i in range(len(s)):
    if s[i]=="{":
        p += 1
    elif s[i]=="}":
        p -= 1
    else:
        if p==1:
            if s[i]==":":
                print("dict")
                exit()
            elif s[i]==",":
                print("set")
                exit()
print("set")
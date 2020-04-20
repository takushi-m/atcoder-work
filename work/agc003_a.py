s = set(list(input()))
if len(s)==4:
    print("Yes")
    exit()
elif len(s)==2:
    if "N" in s and "S" in s:
        print("Yes")
        exit()
    elif "E" in s and "W" in s:
        print("Yes")
        exit()

print("No")
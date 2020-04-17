from string import ascii_lowercase

s = set(list(input()))

for c in ascii_lowercase:
    if c not in s:
        print(c)
        exit()
print("None")
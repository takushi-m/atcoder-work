from collections import Counter

c = Counter(list(input()))

for k in c:
    if c[k]%2==1:
        print("No")
        exit()
print("Yes")
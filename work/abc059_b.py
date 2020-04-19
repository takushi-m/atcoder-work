a = input()
b = input()

if len(a)<len(b):
    print("LESS")
elif len(a)>len(b):
    print("GREATER")
elif a<b:
    print("LESS")
elif a>b:
    print("GREATER")
else:
    print("EQUAL")
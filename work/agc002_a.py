a,b = map(int, input().split())

if min(a,b)<0 and max(a,b)>0:
    print("Zero")
    exit()
if min(a,b)>0:
    print("Positive")
    exit()


c = -min(a,b) - max(a,b) + 1

if c%2==0:
    print("Positive")
else:
    print("Negative")
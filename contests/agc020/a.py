line = input().split(" ")
N = int(line[0])
A = int(line[1])
B = int(line[2])

x = B-A-1

if x%2==0:
    print("Borys")
elif x%2==1:
    print("Alice")

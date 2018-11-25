line = input().split(" ")
a = max(int(line[0])-1,0)
b = max(int(line[1])-1,0)

h = 100
w = 100
m = []

for hi in range(h):
    if hi<50:
        m.append(["#" for _ in range(w)])
    else:
        m.append(["." for _ in range(w)])

for ai in range(a//50):
    for i in range(50):
        m[2*ai][2*i] = "."
for ai in range(a%50):
    m[2*(a//50)][2*ai] = "."

for bi in range(b//50):
    for i in range(50):
        m[50+2*bi+1][2*i] = "#"
for bi in range(b%50):
    m[50+2*(b//50)+1][2*bi] = "#"

print(str(h)+" "+str(w))
for hi in range(h):
    print("".join(m[hi]))

    

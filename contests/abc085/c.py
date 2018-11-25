# coding=utf-8

line = input().split(" ")
N = int(line[0])
Y = int(line[1])

ret = ["-1","-1","-1"]
for z in range(N+1):
    x = (Y-5000*N+4000*z)
    if x%5000==0:
        x = x/5000
        y = N-z-x
        if x>=0 and y>=0:
            ret = [str(int(x)),str(int(y)),str(int(z))]
            break

print(" ".join(ret))

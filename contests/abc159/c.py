l = int(input())

def f(x,y):
    z = l-x-y
    if z<0 or z>l:
        print(x,y,z)
        return -1
    return x*y*z

def fp(x,y):
    dx = y*(l-x-y) - x*y
    dy = x*(l-x-y) - x*y
    return dx,dy

x = 1.0
y = 1.0
while True:
    dx,dy = fp(x,y)
    if abs(dx)<10**-6 and abs(dy)<10**-6:
        print(f(x,y))
        exit()

    x += dx * 10**-5
    y += dy * 10**-5

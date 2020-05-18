from math import sqrt,pi,cos,sin

a,b,h,m = map(int, input().split())

ta = h*2*pi/12 + m*2*pi/(12*60)
tb = m*2*pi/60

xa = a*cos(ta)
ya = a*sin(ta)
xb = b*cos(tb)
yb = b*sin(tb)

print(sqrt((xa-xb)**2 + (ya-yb)**2))
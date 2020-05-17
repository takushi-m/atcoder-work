from math import pi,sin,cos,sqrt

a,b,h,m = map(int, input().split())

ta = h*2.0*pi/12
tb = m*2.0*pi/60

xa = a*cos(ta)
ya = a*sin(ta)
xb = b*cos(tb)
yb = b*sin(tb)

print(sqrt((xa-xb)**2.0 + (ya-yb)**2.0))
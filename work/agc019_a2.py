q,h,s,d = map(int, input().split())
n = int(input())

q = 4*q
h = 2*h
x = min(q,h,s)

print((n//2)*min(2*x,d)+(n%2)*x)
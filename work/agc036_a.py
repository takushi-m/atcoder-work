s = int(input())

x = 10**9 - s%10**9
y = (s+x)//10**9
print(0,0,10**9,1,x,y)
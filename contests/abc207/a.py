a,b,c = map(int, input().split())
print(max(a+b,max(b+c,c+a)))
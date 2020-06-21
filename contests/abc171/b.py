n,k = map(int, input().split())
al = list(map(int, input().split()))
al.sort()
print(sum(al[:k]))
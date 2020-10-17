def calc(n):
    l = []
    i = 1
    while i*i<=n:
        if n%i==0:
            l.append(i)
            if i!=n//i:
                l.append(n//i)
        i += 1
    if len(l)==0 and n==1:
        l.append(1)
    l.sort()
    for x in l:
        print(x)

if __name__ == "__main__":
    n = int(input())
    calc(n)
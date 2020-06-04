q,l = map(int, input().split())

st = []
size = 0
end = False
for _ in range(q):
    line = input().split()
    if end:
        continue
    if line[0]=="Top":
        if size==0:
            print("EMPTY")
            end = True
        else:
            print(st[-1][1])
    elif line[0]=="Size":
        print(size)
    elif line[0]=="Push":
        n,m = int(line[1]),int(line[2])
        if size>l-n:
            print("FULL")
            end = True
        else:
            st.append((n,m))
            size += n
    else:
        n = int(line[1])
        if size<n:
            print("EMPTY")
            end = True
        else:
            size -= n
            while n>0:
                s = st.pop()
                if n==s[0]:
                    break
                if n>s[0]:
                    n -= s[0]
                else:
                    st.append((s[0]-n,s[1]))
                    n = 0
if not end:
    print("SAFE")
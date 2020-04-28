from collections import deque

sa = deque(list(input()))
sb = deque(list(input()))
sc = deque(list(input()))

x = "a"
while True:
    if x=="a" and len(sa)==0:
        print("A")
        exit()
    elif x=="b" and len(sb)==0:
        print("B")
        exit()
    elif x=="c" and len(sc)==0:
        print("C")
        exit()
    
    if x=="a":
        x = sa.popleft()
    elif x=="b":
        x = sb.popleft()
    elif x=="c":
        x = sc.popleft()

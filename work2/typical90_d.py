h,w = map(int, input().split())
al = [list(map(int, input().split())) for _ in range(h)]

rl = [sum(al[hi]) for hi in range(h)]
cl = [sum(al[hi][wi] for hi in range(h)) for wi in range(w)]

bl = [[-al[hi][wi] for wi in range(w)] for hi in range(h)]

for hi in range(h):
    line = []
    for wi in range(w):
        line.append(str(rl[hi]+cl[wi]+bl[hi][wi]))
    print(" ".join(line))
import heapq

x,y,a,b,c = map(int, input().split())
pl = list(map(int, input().split()))
ql = list(map(int, input().split()))
rl = list(map(int, input().split()))

pl.sort(reverse=True)
pl = pl[:x]
heapq.heapify(pl)
ql.sort(reverse=True)
ql = ql[:y]
heapq.heapify(ql)
rl.sort(reverse=True)

for r in rl:
    dp = r-pl[0]
    dq = r-ql[0]
    if dp<=0 and dq<=0:
        break
    if dp>dq:
        heapq.heappushpop(pl,r)
    else:
        heapq.heappushpop(ql,r)

print(sum(pl)+sum(ql))
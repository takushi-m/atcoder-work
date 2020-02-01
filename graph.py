# 二部グラフの判定。連結でなくても良い
# eは隣接リスト。nは要素数
def is_bipartite(e,n):
    col = [-1]*n
    for s in range(n):
        if col[s]>=0:
            continue
        col[s] = 0
        q = [s]
        while len(q)>0:
            v = q.pop()
            c = col[v]
            for u in e[v]:
                if col[u]<0:
                    col[u] = (c+1)%2
                    q.append(u)
                else:
                    if c==col[u]:
                        return False
    return True
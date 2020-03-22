from itertools import combinations
def f(n,s,al):
    res = 0
    for l in range(n):
        for r in range(l,n):
            for k in range(1,r-l+1+1):
                for c in combinations(range(l,r+1),k):
                    if s==sum([al[x] for x in c]):
                        res += 1
    return res


if __name__ == '__main__':
    n,s = map(int, input().split())
    al = list(map(int, input().split()))
    print(f(n,s,al))
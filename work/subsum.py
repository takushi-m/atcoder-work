# coding=utf-8

import unittest

def dfs(a, i, n, sum, k):
    if i==n:
        return sum==k
    if dfs(a, i+1, n, sum, k):
        return True
    if dfs(a, i+1, n, sum+a[i], k):
        return True
    return False


def f(a, k):
    if dfs(a, 0, len(a), 0, k):
        return "Yes"
    else:
        return "No"

def f2(a,k):
    l = [(0,0)]
    while len(l)>0:
        s = l.pop()
        if s[1]==len(a):
            if s[0]==k:
                return "Yes"
            continue
        elif s[0]==k:
            return "Yes"
        l.append((s[0], s[1]+1))
        l.append((s[0]+a[s[1]], s[1]+1))
    return "No"

def f3(a, k):
    dp = []
    for _ in range(10+1):
        dp.append([False for _ in range(100)])
    dp[0][0] = True

    for i in range(10):
        for j in range(100):
            dp[i+1][j]

class TestSubSum(unittest.TestCase):
    def test_1(self):
        self.assertEqual(f([1,2,4,7], 15), "No")
        self.assertEqual(f([1,2,4,7], 6), "Yes")
    def test_2(self):
        self.assertEqual(f2([1,2,4,7], 15), "No")
        self.assertEqual(f2([1,2,4,7], 6), "Yes")


if __name__ == '__main__':
    unittest.main()

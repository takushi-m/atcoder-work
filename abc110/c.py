# -*- coding: utf-8 -*-
import unittest


def func(s,t):
    n = len(s)
    for c in set(s):
        d = None
        for i in range(n):
            if s[i]==c:
                if d is None:
                    d = t[i]
                elif d!=t[i]:
                    return "No"
    for c in set(t):
        d = None
        for i in range(n):
            if t[i]==c:
                if d is None:
                    d = s[i]
                elif d!=s[i]:
                    return "No"
    return "Yes"

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(func("azzel", "apple"), "Yes")
        self.assertEqual(func("chokudai", "redcoder"), "No")
        self.assertEqual(func("abcdefghijklmnopqrstuvwxyz", "ibyhqfrekavclxjstdwgpzmonu"), "Yes")
        self.assertEqual(func("abc", "abc"), "Yes")

if __name__ == '__main__':
    s = input()
    t = input()
    # unittest.main()
    print(func(s,t))

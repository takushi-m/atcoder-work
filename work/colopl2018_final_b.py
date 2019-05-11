# -*- coding: utf-8 -*-
import re
import sys
sys.setrecursionlimit(10**5)
symbol = re.compile("[+\-*/\(,)]")
op1 = re.compile("[+*]")
op2 = re.compile("[\-/]")
num = re.compile("[0-9]+")
s = input()

def tokenize(s):
    res = []
    i = 0
    n = len(s)
    while i<n:
        c = s[i]
        if symbol.match(c):
            res.append(c)
            i += 1
        else:
            d = ""
            while i<n and num.match(s[i]):
                d += s[i]
                i += 1
            res.append(d)
    return res

tokens = tokenize(s)
def term(pos):
    if num.match(tokens[pos]):
        return tokens[pos],pos+1
    elif op2.match(tokens[pos]):
        op = tokens[pos]
        pos += 2
        t1,pos = term(pos)
        pos += 1
        t2,pos = term(pos)
        pos += 1
        return [op,t1,t2],pos
    elif op1.match(tokens[pos]):
        op = tokens[pos]
        pos += 2
        t,pos = term(pos)
        tl = [t]
        while tokens[pos]==",":
            pos += 1
            t,pos = term(pos)
            tl.append(t)
        pos += 1
        return [op]+tl,pos

node,_ = term(0)
def gen(node):
    if type(node) is str:
        return node
    else:
        op = node[0]
        return "("+op.join([gen(n) for n in node[1:]])+")"

print(gen(node))

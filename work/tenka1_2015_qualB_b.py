import sys
sys.setrecursionlimit(10**9)

def token(tk):
    def f(s,pos):
        if s[pos:pos+len(tk)]==tk:
            return [True, tk, pos+len(tk)]
        else:
            return [False, None, pos]
    return f

def integer(s,pos):
    if s[pos] not in "0123456789":
        return [False, None, pos]
    j = pos
    while j<len(s):
        if s[j] not in "0123456789":
            break
        j += 1
    return [True, s[pos:j], j]

def many(parser):
    def f(s, pos):
        res = []
        while True:
            parsed = parser(s,pos)
            if parsed[0]:
                res.append(parsed[1])
                pos = parsed[2]
            else:
                break

        return [True, res, pos]
    return f

def choice(parsers):
    def f(s, pos):
        for p in parsers:
            res = p(s,pos)
            if res[0]:
                return res
        return [False, None, pos]
    return f

def seq(parsers):
    def f(s,pos):
        res = []
        for p in parsers:
            r = p(s,pos)
            if r[0]:
                res.append(r[1])
                pos = r[2]
            else:
                return [False, None, pos]
        return [True, res, pos]
    return f

def lazy(callback):
    parse = None
    def f(s, pos):
        nonlocal parse
        if parse==None:
            parse = callback()
        return parse(s,pos)
    return f

def map(p,fn):
    def parser(target,pos):
        parsed = p(target,pos)
        if parsed[0]:
            return [parsed[0],fn(parsed[1]),parsed[2]]
        else:
            return parsed
    return parser

# DICT = "{" , EXPR , ":" , EXPR , { "," , EXPR , ":" , EXPR } , "}" | "{}" ;
# SET  = "{" , EXPR , { "," , EXPR } , "}" ;
# EXPR = DICT | SET | INTEGER ;

DICT = map(lazy(lambda:choice([seq([
    token("{"),
    EXPR,
    token(":"),
    EXPR,
    many(seq([token(","),EXPR,token(":"),EXPR])),
    token("}")
]), seq([token("{"), token("}")])])), lambda x:["dict",x])
SET = map(lazy(lambda:seq([
    token("{"),
    EXPR,
    many(seq([token(","),EXPR])),
    token("}")
])), lambda x:["set", x])
INTERGER = map(integer, lambda x:["int", x])
EXPR = choice([DICT, SET, INTERGER])

e = EXPR(input(), 0)
print(e[1][0])
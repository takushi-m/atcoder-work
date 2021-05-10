n = int(input())
s = input()

mod = 10**9 + 7
d = {
    "a": 0,
    "at": 0,
    "atc": 0,
    "atco": 0,
    "atcod": 0,
    "atcode": 0,
    "atcoder": 0
}

for c in s:
    if c=="a":
        d["a"] += 1
    elif c=="t":
        d["at"] += d["a"]
        d["at"] %= mod
    elif c=="c":
        d["atc"] += d["at"]
        d["atc"] %= mod
    elif c=="o":
        d["atco"] += d["atc"]
        d["atco"] %= mod
    elif c=="d":
        d["atcod"] += d["atco"]
        d["atcod"] %= mod
    elif c=="e":
        d["atcode"] += d["atcod"]
        d["atcode"] %= mod
    elif c=="r":
        d["atcoder"] += d["atcode"]
        d["atcoder"] %= mod

print(d["atcoder"])
# -*- coding: utf-8 -*-
from string import ascii_lowercase

c = input()

i = 0
while i<100:
    if ascii_lowercase[i]==c:
        print(ascii_lowercase[i+1])
        exit()
    i += 1
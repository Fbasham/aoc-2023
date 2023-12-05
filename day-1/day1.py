import re

with open('data.txt') as f:
    a = [re.findall('\d',s) for s in f.readlines()]
    r = sum(int(t[0]+t[-1]) for t in a)
    print(r)
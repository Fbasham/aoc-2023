with open('data.txt') as f:
    a = [e.split() for e in f.read().splitlines()]

# a = [e.split() for e in '''32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483'''.splitlines()]

# part one
def f(s):
    d = sorted({k:s.count(k) for k in set(s)}.values())
    if d==[5]: e = 6
    elif d==[1,4]: e = 5
    elif d==[2,3]: e = 4
    elif d==[1,1,3]: e =3
    elif d==[1,2,2]: e = 2
    elif d==[1,1,1,2]: e = 1
    else: e = 0
    return e

def g(s,t):
    return [t.find(e) for e in s]

t = sorted(a,key=lambda x:(f(x[0]),g(x[0],'23456789TJQKA')))
r = sum(int(e[1])*i for i,e in enumerate(t,1))


# part two
from itertools import product

def h(s):
    n = s.count('J')
    r = {s}
    for p in product(list('23456789TJQKA'),repeat=n):
        t = list(p)
        x = ''.join(t.pop(0) if e=='J' else e for e in s)
        r.add(x)
    return max(map(f,r))
        
t = sorted(a,key=lambda x: (h(x[0]),g(x[0],'J23456789TQKA')))
r = sum(int(e[1])*i for i,e in enumerate(t,1))
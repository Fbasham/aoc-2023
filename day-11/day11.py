with open('data.txt') as f:
    a = f.read().splitlines()

#     a = '''...#......
# .......#..
# #.........
# ..........
# ......#...
# .#........
# .........#
# ..........
# .......#..
# #...#.....'''.splitlines()
    

# part one
from itertools import *

j = 0
while j<len(a[0]):
    if all(e[j]=='.' for e in a):
        a = [e[:j]+'.'+e[j:] for e in a]
        j += 1
    j += 1

i = 0
while i<len(a):
    if all(e=='.' for e in a[i]):
        a.insert(i,'.'*len(a[i]))
        i += 1
    i += 1

g = [(i,j) for i,t in enumerate(a) for j,e in enumerate(t) if e=='#']
part_one_d = sum(abs(y1-y2)+abs(x1-x2) for (y1,x1),(y2,x2) in combinations(g,2))



# part two
from itertools import *

r = []

for k in range(1,10):
    t = [e[:] for e in a]
    j = 0
    while j<len(t[0]):
        if all(e[j]=='.' for e in t):
            t = [e[:j]+'.'*k+e[j:] for e in t]
            j += k
        j += 1

    i = 0
    while i<len(t):
        if all(e=='.' for e in t[i]):
            for _ in range(k):
                t.insert(i,'.'*len(t[i]))
            i += k
        i += 1


    g = [(i,j) for i,v in enumerate(t) for j,e in enumerate(v) if e=='#']
    d = sum(abs(y1-y2)+abs(x1-x2) for (y1,x1),(y2,x2) in combinations(g,2))
    r.append(d)

diff = [j-i for i,j in zip(r,r[1:])]
mill_expanded_dist = diff[0]*(1000000-2)+part_one_d
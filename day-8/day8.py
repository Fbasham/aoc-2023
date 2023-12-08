with open('data.txt') as f:
    a = f.read().splitlines()

#     a = '''LR

# 11A = (11B, XXX)
# 11B = (XXX, 11Z)
# 11Z = (11B, XXX)
# 22A = (22B, XXX)
# 22B = (22C, 22C)
# 22C = (22Z, 22Z)
# 22Z = (22B, 22B)
# XXX = (XXX, XXX)'''.splitlines()

    dirs,_,*rest = a
    d = {}
    for e in rest:
        k,v = e.split(' = ')
        d[k] = v[1:-1].split(', ')
    

# part one
k = 0
s = 'AAA'
while s!='ZZZ':
    s = d[s][dirs[k%len(dirs)]=='R']
    k += 1
# print(s,k)


# part two
from math import lcm
q = [k for k in d if k[-1]=='A']
t = []
for s in q:
    k = 0
    while s[-1]!='Z':
        s = d[s][dirs[k%len(dirs)]=='R']
        k += 1
    t.append(k)

print(lcm(*t))
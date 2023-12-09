with open('data.txt') as f:
    a = [list(map(int,e.split())) for e in f.read().splitlines()]

#     a = [list(map(int,e.split())) for e in '''0 3 6 9 12 15
# 1 3 6 10 15 21
# 10 13 16 21 30 45'''.splitlines()]

# part one
r = 0
for u in a:
    t = u[:]
    q = u[-1]
    while any(e!=0 for e in t):
        t = [j-i for i,j in zip(t,t[1:])]
        q += t[-1]
    r += q


# part two
r = 0
for u in a:
    t = u[:]
    q = [t[:]]
    while any(e!=0 for e in t):
        t = [j-i for i,j in zip(t,t[1:])]
        q.append(t)
    p = 0
    for w in q[::-1]:
        p = w[0]-p
    r += p 
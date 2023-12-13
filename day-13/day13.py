with open('data.txt') as f:
    a = f.read().split('\n\n')


def f(s):
    a = s.splitlines()
    for i in range(1,len(a)):
        if list(zip(a[i:],a[:i][::-1])) and all(x==y for x,y in zip(a[i:],a[:i][::-1])):
            return (100,i)

    t = list(zip(*a))
    for i in range(1,len(t)):
        if list(zip(t[i:],t[:i][::-1])) and all(x==y for x,y in zip(t[i:],t[:i][::-1])):
            return (1,i)

def part_one():
    return sum(i*j for i,j in map(f,a))



def ff(s):
    a = s.splitlines()
    r = set()
    for i in range(1,len(a)):
        if list(zip(a[i:],a[:i][::-1])) and all(x==y for x,y in zip(a[i:],a[:i][::-1])):
            r.add((100,i))

    t = list(zip(*a))
    for i in range(1,len(t)):
        if list(zip(t[i:],t[:i][::-1])) and all(x==y for x,y in zip(t[i:],t[:i][::-1])):
            r.add((1,i))

    return r

def g(m,p):
    a = [list(e) for e in m.splitlines()]
    s = set()
    for i in range(len(a)):
        for j in range(len(a[0])):
            t = [e[:] for e in a[:]]
            t[i][j] = '.' if t[i][j]=='#' else '#'
            t = '\n'.join(''.join(e) for e in t)
            r = ff(t)
            s |= r
    return s

def part_two():
    r = 0
    for m in a:
        p1 = f(m)
        i,j = next(iter(g(m,p1)-{p1}))
        r += i*j
    return r

print(part_two())
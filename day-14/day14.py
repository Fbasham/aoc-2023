with open('data.txt') as f:
    a = f.read().splitlines()

# a = '''O....#....
# O.OO#....#
# .....##...
# OO.#O....O
# .O.....O#.
# O.#..O.#.#
# ..O..#O..O
# .......O..
# #....###..
# #OO..#....'''.splitlines()


def part_one(a):

    def f(s):
        o = 'O'*(s.count('O'))
        return '.'*(len(s)-len(o))+o

    t = ['#'.join(f(x) for x in ''.join(e)[::-1].split('#')) for e in list(zip(*a))]
    return sum(sum(i+1 for i,e in enumerate(s) if e=='O') for s in t)



def part_two():
    
    def f(s):
        o = 'O'*(s.count('O'))
        return '.'*(len(s)-len(o))+o

    t = a[:]
    v = [t[:]]
    while len(v)<1000:
        t = ['#'.join(f(x) for x in ''.join(e)[::-1].split('#')) for e in list(zip(*t))]
        if t in v: break
        v.append(t[:])
    return part_one(v[1000000000%len(v)])

print(part_two())
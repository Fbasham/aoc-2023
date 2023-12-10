with open('data.txt') as f:
    a = f.read().splitlines()

#     a = '''..F7.
# .FJ|.
# SJ.L7
# |F--J
# LJ...'''.splitlines()

# F-7
# | |
# L-J
d = {
    '|': {(-1,0):'|7F',(1,0):'|LJ',(0,-1):'',(0,1):''},
    '-': {(-1,0):'',(1,0):'',(0,-1):'-LF',(0,1):'-J7'},
    'L': {(-1,0):'|7F',(1,0):'',(0,-1):'',(0,1):'-J7'},
    'J': {(-1,0):'|7F',(1,0):'',(0,-1):'-LF',(0,1):''},
    '7': {(-1,0):'',(1,0):'|LJ',(0,-1):'-LF',(0,1):''},
    'F': {(-1,0):'',(1,0):'|LJ',(0,-1):'',(0,1):'-J7'},
}


# part one
def part_one():
    i,j = next((i,j) for i,t in enumerate(a) for j,e in enumerate(t) if e=='S')
    y,x = 22,90  # cheese (based on i,j above and looking around to find a 'nice' starting point)
    v = [(i,j)]
    while a[y][x]!='S':
        v.append((y,x))
        k = a[y][x]
        dd = d[k]
        for dy,dx in dd:
            if dd[(dy,dx)]:
                i,j = y+dy,x+dx
                if 0<=i<len(a) and 0<=j<len(a[0]) and a[i][j] in dd[(dy,dx)] and (i,j) not in v:
                    y,x = i,j
                    break
        else:
            break

    return len(v)//2


# a = '''..........
# .S------7.
# .|F----7|.
# .||OOOO||.
# .||OOOO||.
# .|L-7F-J|.
# .|II||II|.
# .L--JL--J.
# ..........'''.splitlines()

# part two
def part_two():
    t = list(map(list,a))
    i,j = next((i,j) for i,t in enumerate(a) for j,e in enumerate(t) if e=='S')
    y,x = 22,90  # cheese (based on i,j above and looking around to find a 'nice' starting point)
    v = [(i,j)]
    while a[y][x]!='S':
        v.append((y,x))
        k = a[y][x]
        dd = d[k]
        for dy,dx in dd:
            if dd[(dy,dx)]:
                i,j = y+dy,x+dx
                if 0<=i<len(a) and 0<=j<len(a[0]) and a[i][j] in dd[(dy,dx)] and (i,j) not in v:
                    y,x = i,j
                    break
        else:
            break

    for i in range(len(t)):
        for j in range(len(t[0])):
            if (i,j) not in v:
                t[i][j] = '.'
            else:
                t[i][j] = {
                        '|': '┃',
                        '-': '━',
                        'L': '┗',
                        'J': '┛',
                        '7': '┓',
                        'F': '┏',
                }.get(t[i][j],t[i][j])

    for e in t:
        print(''.join(e))

# cheese it and count...
print(part_two())
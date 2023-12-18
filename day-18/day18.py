with open('data.txt') as f:
    a = f.read().splitlines()

# a = '''R 6 (#70c710)
# D 5 (#0dc571)
# L 2 (#5713f0)
# D 2 (#d2c081)
# R 2 (#59c680)
# D 2 (#411b91)
# L 5 (#8ceee2)
# U 2 (#caa173)
# L 1 (#1b58a2)
# U 2 (#caa171)
# R 2 (#7807d2)
# U 3 (#a77fa3)
# L 2 (#015232)
# U 2 (#7a21e3)'''.splitlines()


def part_one():
    l = 900
    t = [[' ' for _ in range(l)] for _ in range(l)]
    y=x=l>>1

    d = {'R':(0,1),'L':(0,-1),'U':(-1,0),'D':(1,0)}
    my,ny,mx,nx = 1e6,0,1e6,0
    for s in a:
        k,v,c = s.split()
        dy,dx = d[k]
        my = min(my,y)
        ny = max(ny,y)
        mx = min(mx,x)
        nx = max(nx,x)
        for _ in range(int(v)):
            t[y][x] = '#'
            y,x = y+dy,x+dx

    t = [e[mx:nx+1] for e in t[my:ny+1]]
    ty = next(i for i,e in enumerate(t) if e.count('#')==2)
    tx = t[ty].index('#')
    q = [(ty+1,tx+1)]
    while q:
        y,x = q.pop()
        if t[y][x]=='#': continue
        t[y][x] = '#'
        for i,j in ((y-1,x),(y+1,x),(y,x-1),(y,x+1)):
            if 0<=i<len(t) and 0<=j<len(t[0]) and t[i][j]==' ':
                q.append((i,j))

    return '\n'.join(map(''.join,t)).count('#')


print(part_one())
with open('data.txt') as f:
    a = f.read().splitlines()

# a = '''.|...\....
# |.-.\.....
# .....|-...
# ........|.
# ..........
# .........\\
# ..../.\\\\..
# .-.-/..|..
# .|....-|.\\
# ..//.|....'''.splitlines()

def part_one(y=0,x=0,dy=0,dx=1):
    r = set()
    q = [[y,x,dy,dx]]
    while q:
        y,x,dy,dx = q.pop()
        if (y,x,dy,dx) in r or (y<0 or y>=len(a) or x<0 or x>=len(a[0])):
            continue
        r.add((y,x,dy,dx))

        if a[y][x]=='|' and dy==0 and abs(dx)==1: 
            q.append([y-1,x,-1,0])
            q.append([y+1,x,1,0])
        elif a[y][x]=='-' and abs(dy)==1 and dx==0:
            q.append([y,x-1,0,-1])
            q.append([y,x+1,0,1])
        elif a[y][x]=='/' and dy==0 and dx==1:
            q.append([y-1,x,-1,0])
        elif a[y][x]=='/' and dy==0 and dx==-1:
            q.append([y+1,x,1,0])
        elif a[y][x]=='/' and dy==1 and dx==0:
            q.append([y,x-1,0,-1])
        elif a[y][x]=='/' and dy==-1 and dx==0:
            q.append([y,x+1,0,1])
        elif a[y][x]=='\\' and dy==0 and dx==1:
            q.append([y+1,x,1,0])
        elif a[y][x]=='\\' and dy==0 and dx==-1:
            q.append([y-1,x,-1,0])
        elif a[y][x]=='\\' and dy==1 and dx==0:
            q.append([y,x+1,0,1])
        elif a[y][x]=='\\' and dy==-1 and dx==0:
            q.append([y,x-1,0,-1])
        else:
            q.append([y+dy,x+dx,dy,dx])

    s = {(y,x) for y,x,dy,dx in r}
    return len(s)


def part_two():
    r = 0
    for y in range(len(a)):
        r = max(r,part_one(y,0,0,1),part_one(len(a)-y-1,0,0,-1))
    for x in range(len(a[0])):
        r = max(r,part_one(0,x,1,0),part_one(len(a[0])-x-1,0,-1,0))
    return r

print(part_one())
print(part_two())
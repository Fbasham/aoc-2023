# part one
with open('data.txt') as f:
    import re

    a = f.read().splitlines()
    r = 0
    for y,s in enumerate(a):
        t = s.strip()
        for m in re.findall('\d+',t):
            i = t.find(m)
            f = 0
            for x in range(i,i+len(m)):
                for dy,dx in ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)):
                    yy,xx = y+dy,x+dx
                    if 0<=yy<len(a) and 0<=xx<len(a[yy]) and a[yy][xx] not in '.1234567890':
                        f = 1
                        break
                if f: break
            if f:
                t = t.replace(m,'.'*len(m),1)
                r += int(m)


# part two
with open('data.txt') as f:
    import re
    from math import prod

    a = f.read().splitlines()
    d = {}
    dd = {}
    for y,s in enumerate(a):
        t = s.strip()
        for m in re.findall('\d+',t):
            i = t.find(m)
            f = 0
            for x in range(i,i+len(m)):
                for dy,dx in ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)):
                    yy,xx = y+dy,x+dx
                    if 0<=yy<len(a) and 0<=xx<len(a[yy]) and a[yy][xx] not in '.1234567890':
                        f = 1
                        break
                if f: break
            if f:
                for k,e in enumerate(m):
                    d[(y,i+k)] = m
                    dd.setdefault(m,[]).append((y,i+k))
                t = t.replace(m,'.'*len(m),1)
    
    r = 0
    for y,s in enumerate(a):
        for x,e in enumerate(s):
            if re.match('[^\d.]',e):
                t = set()
                for dy,dx in ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)):
                    i,j = y+dy,x+dx
                    if 0<=i<len(a) and 0<=j<len(a[i]) and a[i][j].isdigit():
                        t.add(d[(i,j)])

                if len(t)==2:
                    r += prod(map(int,t))
    
    print(r)
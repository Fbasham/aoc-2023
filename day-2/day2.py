# part one
with open('data.txt') as f:
    r = 0
    for s in f.readlines():
        g,u = s.split(': ')
        t = u.split('; ')
        for ss in t:
            d = {}  
            for e in ss.strip().split(', '):
                d[e.split()[1]] = int(e.split()[0])       
            if d.get('red',0)>12 or d.get('green',0)>13 or d.get('blue',0)>14:
                break
        else:
            r += int(g[5:])


# part two
with open('data.txt') as f:
    from math import prod
    r = 0
    for s in f.readlines():
        g,u = s.split(': ')
        t = u.split('; ')
        d = {}  
        print(t) 
        for ss in t:
            for e in ss.strip().split(', '):
                k = e.split()[1]
                d[k] = max(d.get(k,0),int(e.split()[0]))    
        r += prod(d.values())
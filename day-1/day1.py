import re

# part one
with open('data.txt') as f:
    a = [re.findall('\d',s) for s in f.readlines()]
    r = sum(int(t[0]+t[-1]) for t in a)
    print(r)


#part 2
with open('data.txt') as f:
    # there's overlap in some of the lines...
    d = 'one two three four five six seven eight nine'.split()
    def g(m):
        t = [e.group(1) for e in m]
        return [k if k.isdigit() else str(d.index(k)+1) for k in t]
    a = [g(re.finditer(f"(?=({'|'.join(d+list('123456789'))}))",s)) for s in f.readlines()]
    r = sum(int(t[0]+t[-1]) for t in a)